#!/usr/bin/python3
"""Set Django admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively
    --domain=   unless provided, will ask interactively
                DEFAULT=www.example.com

"""

import sys
import getopt
import inithooks_cache
import hashlib
import random
import os

from dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

DEFAULT_DOMAIN="www.example.com"

  
def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email=', 'domain='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    email = ""
    domain = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val
        elif opt == '--domain':
            domain = val



    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Django Password",
            "Enter new password for the Django 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Django Email",
            "Enter email address for the Django 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    if not domain:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        domain = d.get_input(
            "Django Domain",
            "Enter the domain to serve Django.",
            DEFAULT_DOMAIN)

    if domain == "DEFAULT":
        domain = DEFAULT_DOMAIN

    inithooks_cache.write('APP_DOMAIN', domain)
    

    m = MySQL()
    m.execute('UPDATE django.auth_user SET email=%s WHERE username=\"admin\";', (email,))
    os.system("echo \"from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.set_password('"+ password + "');user.save()\" | /var/www/turnkey_project/manage.py shell")
  
    with open('/var/lib/django/allowed_hosts', 'w') as fob:
        fob.write("*" + '\n')
        fob.write(domain + '\n')

if __name__ == "__main__":
    main()

