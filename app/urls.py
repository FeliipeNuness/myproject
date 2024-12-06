
from django.contrib import admin
from django.urls import path
from backend.views import CategoryCreateListView, CategoryRetrieveUpdateDestroyView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', CategoryCreateListView.as_view(), name='category-create-list'),
    path('category/<int:pk>', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail-view'),
]
