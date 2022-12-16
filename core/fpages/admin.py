from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.cintrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _


class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced_options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

