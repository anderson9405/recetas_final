from django import forms

class crearNuevaReceta(forms.Form):
    nombre= forms.CharField(label = "Nombre de la receta", max_length=200)
    ingredientes= forms.CharField(label = "Ingrese los ingredientes de la receta", widget=forms.Textarea)
    descripcion= forms.CharField(label = "Ingrese los pasos para preparar la receta", widget=forms.Textarea)