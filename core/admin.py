from django.contrib import admin
from .models import Category, Door

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

@admin.register(Door)
class DoorAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    list_per_page = 20
    readonly_fields = ('image_preview',)
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'price', 'description')
        }),
        ('Image', {
            'fields': ('image', 'image_preview')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 200px;" />'
        return "No Image"
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'
