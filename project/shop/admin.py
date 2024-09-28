from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'unit_price', 'in_stock', 'category']
    list_display_links = ['id', 'title']
    list_editable = ['unit_price', 'in_stock']
    prepopulated_fields = {'slug': ['title',]}