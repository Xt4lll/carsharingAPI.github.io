from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets, status, generics
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response



class CarViewset(APIView):
    def get(self, request, id=None):
        if id:
            item = models.Car.objects.get(id=id)
            serializer = serializers.CarSerializer(item)
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        
        items = models.Car.objects.all()
        serializer = serializers.CarSerializer(items, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = serializers.CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status':'error', 'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, id=None):
        item = models.Car.objects.get(id=id)
        serializer = serializers.CarSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status':'error', 'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id=None):
        item = models.Car.objects.filter(id=id)
        print(item)
        item.delete()
        return Response({'status': 'success', 'data': 'item deleted'})
    