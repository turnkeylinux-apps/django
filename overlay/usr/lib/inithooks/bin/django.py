#!/usr/bin/python
"""Set Django admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
import inithooks_cache
import hashlib
import random

from dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def _get_hashpass(password):
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    hash = hashlib.sha1(salt + password).hexdigest()
    return 'sha1$%s$%s' % (salt, hash)
    
def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

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
    
    hashpass = _get_hashpass(password)

    m = MySQL()
    m.execute('UPDATE django.auth_user SET email=\"%s\" WHERE username=\"admin\";' % email)
    m.execute('UPDATE django.auth_user SET password=\"%s\" WHERE username=\"admin\";' % hashpass)

if __name__ == "__main__":
    main()

