
from django.urls import path
from . import views


urlpatterns = [
    path('policy/', views.privacy, name="privacy"),
]
