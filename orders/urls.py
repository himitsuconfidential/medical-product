from django.urls import path
from orders import views

urlpatterns = [
    path('hello', views.hello),
    path('view_all', views.ViewAll.as_view()),
]
