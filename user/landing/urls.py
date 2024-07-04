from user.landing import views
from django.urls import path

urlpatterns = [
    path('user/contact/', views.UserContactView.as_view())
]
