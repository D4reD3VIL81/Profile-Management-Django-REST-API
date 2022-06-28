from django.urls import path
from . import views

app_name = ''

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]