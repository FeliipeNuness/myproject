from django.contrib import admin
from backend.models import Category, Product
from plans.models import Plan, Signature


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'category', 'user')
    
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'periodicity')
   
    
@admin.register(Signature)    
class SignatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plan', 'start_date', 'end_date', 'status')

