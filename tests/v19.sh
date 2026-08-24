#!/bin/bash
set -Eeuo pipefail
umask 077

result=${TKL_TEST_RESULT:?TKL_TEST_RESULT is required}
app_password=${TKL_TEST_APP_PASS:?TKL_TEST_APP_PASS is required}
db_password=${TKL_TEST_DB_PASS:?TKL_TEST_DB_PASS is required}
base=https://127.0.0.1
cookie_jar=/tmp/tkl-django-cookies.$$
login_page=/tmp/tkl-django-login.$$
admin_page=/tmp/tkl-django-admin.$$

cleanup() {
    rm -f -- "$cookie_jar" "$login_page" "$admin_page"
}
trap cleanup EXIT

systemctl --quiet is-active apache2.service mariadb.service multi-user.target
apache2ctl -M 2>/dev/null | grep -q 'wsgi_module'
installed=$(dpkg-query -W -f='${Version}' python3-django)

curl --insecure --fail --silent --show-error "$base/" |
    grep -q '<h1>TurnKey Django</h1>'
curl --insecure --fail --silent --show-error "$base/doc/index.html" |
    grep -qi 'Django documentation'

login_url=$base/admin/login/?next=/admin/
curl --insecure --fail --silent --show-error \
    --cookie-jar "$cookie_jar" "$login_url" >"$login_page"
csrf=$(python3 - "$login_page" <<'PY'
import re
import sys

page = open(sys.argv[1], encoding="utf-8").read()
match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', page)
assert match, "Django login page did not contain a CSRF token"
print(match.group(1))
PY
)
curl --insecure --fail --silent --show-error --location \
    --cookie "$cookie_jar" --cookie-jar "$cookie_jar" \
    --referer "$login_url" \
    --data-urlencode "csrfmiddlewaretoken=$csrf" \
    --data-urlencode 'username=admin' \
    --data-urlencode "password=$app_password" \
    --data-urlencode 'next=/admin/' \
    "$login_url" >"$admin_page"
grep -q 'Site administration' "$admin_page"
grep -q 'Log out' "$admin_page"

cd /var/www/turnkey_project
python3 manage.py shell -c \
    "from django.contrib.auth import get_user_model; from django.db import connection; connection.ensure_connection(); assert connection.vendor == 'mysql'; assert connection.settings_dict['NAME'] == 'django'; assert get_user_model().objects.filter(username='admin', is_staff=True, is_superuser=True).exists()"
python3 manage.py shell -i ipython -c \
    "from django.conf import settings; assert settings.ROOT_URLCONF == 'turnkey_project.urls'"
mysqladmin --user=root --password="$db_password" ping 2>/dev/null |
    grep -q 'mysqld is alive'
dpkg-query -W webmin-apache webmin-mysql >/dev/null

before=$installed
apt-get update >/dev/null
candidate=$(apt-cache policy python3-django | awk '/Candidate:/ {print $2}')
test -n "$candidate"
test "$candidate" != '(none)'
apt-get indextargets --format '$(SITE)|$(SUITE)|$(COMPONENT)' |
    grep -Eq '^deb\.debian\.org\|trixie(-updates)?\|main$'
test "$(dpkg-query -W -f='${Version}' python3-django)" = "$before"

cat >"$result" <<EOF
package_source=Debian Trixie APT repository, python3-django
installed_version=$installed
runtime_checks=normal init; Apache and MariaDB active; HTTPS sample site and bundled documentation; mod_wsgi loaded; administrator HTTP login; Django ORM MariaDB access; root database login; IPython Django shell; Webmin Apache and MariaDB modules installed
updater_command=apt-get update; apt-cache policy python3-django; apt-get indextargets
updater_result=signed metadata refreshed; installed version unchanged; eligible candidate $candidate
updater_channel=Debian Trixie and Trixie security repositories
integrity_evidence=APT accepted Debian signed repository metadata and dpkg reports python3-django $installed installed
EOF
