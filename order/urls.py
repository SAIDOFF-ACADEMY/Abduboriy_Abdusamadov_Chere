from django.urls import path
from order import views

urlpatterns = [
    path('orders/', views.AdminOrderView.as_view()),
    path('order/<int:pk>/', views.AdminOrderGetView.as_view()),
    path('order/update/<int:pk>/', views.AdminOrderUpdateView.as_view()),
    # path('order/delete/<int:pk>', views.AdminOrderDeleteView.as_view()),
]
