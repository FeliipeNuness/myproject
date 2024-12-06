from rest_framework import generics, views, response, status
from rest_framework.response import Response
from backend.models import Category, Product, Transactions, Signature, Plan
from .serializers import CategorySerializer, ProductSerializer, Transactions, SignatureSerializer, PlanSerializer


class CategoryCreateListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer