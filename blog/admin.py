from django.contrib import admin
from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'parent', 'publicated')}),
        ('SEO', {
            'classes': ('collapse', ),
            'fields': ('slug', 'keywords', 'description')})
    )


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'publicated', 'preview_image', 'content')}),
        ('SEO', {
            'classes': ('collapse', ),
            'fields': ('slug', 'keywords', 'description')})
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

