from rest_framework import serializers
from backend.models import Category, Product
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = '__all__' #CASO NÂO QUEIRA MOSTRAR A CATEGORY NO CORPO DO JSON, DEIXE O FIELDS ASSIM:
                            #fields = ['id', 'name', 'description']  # Remova 'product' dos campos


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
   
   
