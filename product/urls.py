from django.urls import path
from product import views

urlpatterns = [
    path('products/', views.ProductView.as_view()), 
    path('product/<int:pk>/', views.ProductGetView.as_view()),
    path('product/create/', views.ProductCreateView.as_view()),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view()),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('free-products/', views.FreeProductView.as_view()),
    path('free-product/<int:pk>/', views.FreeProductGetView.as_view()),
    path('free-product/create/', views.FreeProductCreateView.as_view()),
    path('free-product/delete/<int:pk>/', views.FreeProductDeleteView.as_view()),
    path('free-product/update/<int:pk>/', views.FreeProductUpdateView.as_view()),
]
