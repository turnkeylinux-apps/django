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
- Preconfigured example Django project located at /var/www/turnkey_project
   
   - Integrated with Apache2 (mod\_wsgi), MySQL and Postfix.
   - Built-in administration console with embedded online documentation.

- iPython for enhanced Django shell interaction.
- Webmin modules for configuring Apache2, and MySQL.

Credentials *(passwords set at first boot)*
-------------------------------------------

- Webmin, SSH, MySQL: username **root**
- Django admin console: username **admin**

.. _Django: http://www.djangoproject.com/
.. _TurnKey Core: http://www.turnkeylinux.org/core
