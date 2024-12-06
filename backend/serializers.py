from rest_framework import serializers
from backend.models import Category, Product, Transactions, Plan, Signature
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
   category = CategorySerializer(read_only=True)
   category_id = serializers.PrimaryKeyRelatedField(
       queryset=Category.objects.all(),
       source='category',
       write_only=True
       )
   
   class Meta:
       model = Product
       fields = '__all__'
   
   
class TransactionsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
        )
    
    class Meta:
        model = Transactions
        fields = '__all__'
        

class PlanSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Plan
        fields = '__all__'  
        
 
class SignatureSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    flat = PlanSerializer(read_only=True) 
    flat_id = serializers.PrimaryKeyRelatedField(
        queryset=Plan.objects.all(),
        source='flat',
        write_only=True
        )
    
    class Meta:
        model = Signature
        fields = '__all__'            