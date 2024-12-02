from django.contrib import admin
from .models import Category, Product, Transactions, Flat, Signature


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    list_per_page = 25
    