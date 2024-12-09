
from django.contrib import admin
from django.urls import path, include
from backend.views import CategoryCreateListView, CategoryRetrieveUpdateDestroyView, ProductCreateListView, ProductRetrieveUpdateDestroyView
from plans.views import ListPlansViews
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', CategoryCreateListView.as_view(), name='category-create-list'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail-view'),
    path('product/', ProductCreateListView.as_view(), name='product-detail-view'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-create-list'),
    path('planos/',ListPlansViews.as_view(), name='plans-list-view'),
]
