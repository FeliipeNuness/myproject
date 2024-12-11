from django.contrib import admin
from django.urls import path, include
from backend.views import CategoryCreateListView, CategoryRetrieveUpdateDestroyView, ProductCreateListView, ProductRetrieveUpdateDestroyView
from django.conf.urls.static import static
from plans.views import SubscribeView, PlanCreateListView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URL para criação e listagem de categorias
    path('category/', CategoryCreateListView.as_view(), name='category-create-list'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail-view'),
    
    # URL para criação e listagem de produtos
    path('product/', ProductCreateListView.as_view(), name='product-create-list'),  
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail-view'),  
    
    # URL para listar os planos disponiveis
    path('plans', PlanCreateListView.as_view(), name='plan-list-view'),
    

]
