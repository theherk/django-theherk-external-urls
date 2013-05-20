TheHerk External URLs
=====================

TheHerk External URLs is a tool that allows linking menu items in Django-cms to external URLs.

Usage
-----

1. Add "menu_external_urls" to your INSTALLED_APPS

        INSTALLED_APPS = (
            ...
            'menu_external_urls',
        )

2. Run `python manage.py migrate menu_external_urls`.

   Alternately, you could `syncdb` and `migrate --fake`
