# FORMULARIO PARA AGREGAR Y ACTUALIZAR 
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from .models import *

class ProductoForm (ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Ingrese Nombre"}))
    precio = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Precio"}))
    stock = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Stock"}))
    descripcion = forms.CharField(min_length=10,max_length=200,widget=forms.Textarea(attrs={"rows":4}))

    class Meta:
        model = Producto
        #fields = ['nombre','precio','stock','descripcion','tipo']
        fields = '__all__'

        widgets = {
                'fecha' : forms.SelectDateWidget(years=range(1940,2023))
        }


class RegistroForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']


class CantidadForm (ModelForm):
    cantidad = forms.IntegerField(min_value=1 ,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Cantidad"}))

    class Meta:
        model = Carrito
        fields = ['cantidad']

"""
class CarritoForm (ModelForm):
    cliente = forms.CharField()
    producto = forms.IntegerField()
    cantidad = forms.IntegerField(min_value=1, max_value=5 ,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Cantidad"}))

    class Meta:
        model = Carrito
        fields = ['cantidad']
"""

class envioForm (ModelForm):
    direccion = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Ingrese Dirección"}))
    contacto = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Ingrese Contacto"}))

    class Meta:
        model = Compras
        fields = ['direccion','contacto']


class dpForm (ModelForm):
    rut = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Rut"}))
    primer_nombre = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Primer nombre"}))
    segundo_nombre = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Segundo nombre"}))
    primer_apellido = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Primer apellido"}))
    segundo_apellido = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Segundo apellido"}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Dirección"}))
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    telefono = forms.IntegerField(min_value=1 ,widget=forms.NumberInput(attrs={"placeholder":"Telefono"}))
    correo = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Correo"}))
    comuna = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Comuna"}))
    genero = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Genero"}))
    class Meta:
        model = AdultoMayor
        fields = ['rut','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','direccion','fecha_nacimiento','telefono','correo','comuna','genero']