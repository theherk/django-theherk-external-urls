from cms.admin.pageadmin import PageAdmin
from cms.models.pagemodel import Page
from django.contrib import admin

from menu_external_urls.models import MenuExternalUrl


class MenuExternalUrlAdmin(admin.TabularInline):
    """
    Adds field for Menu External URL
    """
    model = MenuExternalUrl
    fieldsets = (
        ('Menu External URL', {
            'fields': ('menu_external_url',),
        }),
    )

PageAdmin.inlines.append(MenuExternalUrlAdmin)
admin.site.unregister(Page)
admin.site.register(Page, PageAdmin)
