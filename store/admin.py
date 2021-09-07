from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'weight', 'slug',
                    'price', 'quantity_available',
                    'created', 'updated']
    list_filter = ['category']
    list_editable = ['price' ]
    prepopulated_fields = {'slug': ('title', )}

# Register your models here.
