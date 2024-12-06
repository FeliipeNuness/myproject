from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Transactions(models.Model):
    TIPOS = [
        ('entrada', 'saida'),
        ('saida', 'Saída')
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    date =  models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.type} - {self.product.name} - {self.amount}" 
    
class Plan(models.Model):
    name = models.CharField(max_length=200)
    monthly_price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    
class Signature(models.Model):
     user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
     flat = models.ForeignKey(Plan, on_delete=models.CASCADE)
     start_date = models.DateTimeField(auto_now_add=True)
     end_date = models.DateTimeField(blank=True, null=True)
     
     def __str__(self):
         return f"{self.user.name} - {self.plan.name}"
     