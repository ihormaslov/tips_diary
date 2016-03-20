from django.contrib import admin
from page.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'publicated', 'content')}),
        ('SEO', {
            'classes': ('collapse', ),
            'fields': ('slug', 'description')})
    )


admin.site.register(Page, PageAdmin)

