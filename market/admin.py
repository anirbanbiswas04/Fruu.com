from django.contrib import admin
from .models import Category, Listing


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ListingAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_by', 'location', 'created_at']
    list_filter = ['category', 'created_by', 'location']
    search_fields = ['name', 'description', 'location']
    exclude = ('slug',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Listing, ListingAdmin)