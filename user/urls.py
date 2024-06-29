from django.urls import path
from user import views

urlpatterns = [
    path('token/', views.LoginView.as_view()),
    path('email/', views.EmailView.as_view())
]
