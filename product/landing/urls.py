from django.urls import path
from product.landing import views

urlpatterns = [
    path('products/', views.ProductView.as_view())
]
