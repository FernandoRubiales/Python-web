from django.urls import path
from PaginawebApp import views


urlpatterns = [
    
    path("inicio", views.inicio, name="Inicio"),

]