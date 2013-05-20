TheHerk External URLs
=====================

TheHerk External URLs is a tool that allows linking menu items in Django-cms to external URLs.

Usage
-----

1. Add "external_urls" to your INSTALLED_APPS

        INSTALLED_APPS = (
            ...
            'external_urls',
        )

2. Run `python manage.py migrate external_urls`.

   Alternately, you could `syncdb` and `migrate --fake`
