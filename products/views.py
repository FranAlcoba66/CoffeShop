from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

# Create your views here.
class ProductListView(ListView):
    model= Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductListAPI(APIView):
    autehtication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductCreateAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductUpdateAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Product.DoesNotExist:
            return Response(status=404)

class ProductDeleteAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response(status=204)
        except Product.DoesNotExist:
            return Response(status=404)