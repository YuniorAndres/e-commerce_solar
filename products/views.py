# from django.shortcuts import render

# Create your views here.
# products/views.py
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# Vista para listar y crear productos
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
# Agrega esta para ver, actualizar o eliminar por ID
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    