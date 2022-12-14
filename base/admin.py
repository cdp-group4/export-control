from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from base.models import ExtendedFlatPage
from django.utils.translation import gettext_lazy as _


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "url",
                    "title",
                    "title_no",
                    "description",
                    "description_no",
                    "page_content",
                    "page_content_no",
                    "sidebar_title",
                    "sidebar_title_no",
                    "sidebar_text",
                    "sidebar_text_no",
                    "image",
                )
            },
        ),
        (
            _("Advanced options"),
            {
                "classes": ("collapse",),
                "fields": (
                    "enable_comments",
                    "registration_required",
                    "template_name",
                ),
            },
        ),
    )


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.unregister(Site)
admin.site.register(ExtendedFlatPage, FlatPageAdmin)
