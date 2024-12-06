from django.contrib import admin
from backend.models import Category, Product, Transactions, Plan, Signature


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'category', 'user')
    

@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('TIPOS', 'product', 'type', 'amount', 'date', 'user')
    

@admin.register(Plan)        
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'monthly_price', 'description', 'active')
    

@admin.register(Signature)    
class SignatureAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'start_date', 'end_date')