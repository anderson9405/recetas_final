from django.urls import path, include
from miapp import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('recetas/', views.recetas ,name= 'recetas'),
    path('crear_receta/', views.crear_receta, name= 'crear_receta'),
    path('receta_detalle/<int:id>', views.recetas_detalle, name= 'recetas_detalle'),

]