Django - High-level Python Web Framework
========================================

`Django`_ is a high-level Python Web framework that encourages rapid
development and clean, pragmatic design. Python's equivalent to the
famous Ruby on rails, Django lets you build high-performing, elegant Web
applications quickly. Django focuses on automating as much as possible
and adhering to the "Don't Repeat Yourself" (DRY) principle.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- SSL support out of the box.
- Preconfigured Django 4.2 example project located at
  ``/var/www/turnkey_project``.
   
   - Integrated with Apache2 (mod\_wsgi), MariaDB and Postfix.
   - Built-in administration console with embedded online documentation.

- Python 3 build of Django installed from Debian repositories.
- IPython for enhanced Django shell interaction.
- Webmin modules for configuring Apache2 and MariaDB.

Credentials *(passwords set at first boot)*
-------------------------------------------

- Webmin, SSH, MariaDB: username **root**
- Django admin console: username **admin**

.. _Django: http://www.djangoproject.com/
.. _TurnKey Core: https://www.turnkeylinux.org/core
