from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import MyTokenObtainPairSerializer, UserSerializer

class MyTokenObtainPairView(APIView):
    serializer_class = MyTokenObtainPairSerializer

# User CRUD
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Quiz():
    pass
    
# class UserViewSet(APIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
#     def post(self, request):
#         serializer = UserSerializer(data = request.data)
#         if serializer.is_valid():
#             user = serializer.save(request)