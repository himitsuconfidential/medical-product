from django.urls import path
from orders import views

urlpatterns = [
    path('hello', views.hello),
]
