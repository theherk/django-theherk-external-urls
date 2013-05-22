from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pagemodel import Page


class MenuExternalUrl(models.Model):
    """
    Defines External URL for page
    """
    page = models.OneToOneField(Page)
    menu_external_url = models.CharField(
        _('External URL'),
        max_length=200,
        blank=True
    )
