from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework import viewsets, renderers, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import MyTokenObtainPairSerializer, UserSerializer

def find_user(email):
    return User.objects.filter(email = email)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    # required for set_token to user's cookie
    #
    #

# User CRUD
class UserViewSet(viewsets.ModelViewSet):   
    queryset = User.objects.all()
    serializer_class = UserSerializer

# About Sign U and D
class AuthViewSet(APIView):
    # log-in: sign-in
    def post(self, request):
        input_email = request.data['email']
        input_password = request.data['password']
        success = 'success'
        data = {
            success: 'no',
        }
        hi = find_user(input_email)
        if hi[0].password == input_password:
            data[success] = success
            return Response(data[success])
        else:
            return Response(data[success])
    
    # log-out: sign-out
    def delete(self, request):
        response = Response({
            "message": "Logout success"
        }, status = status.HTTP_202_ACCEPTED)
        response.delete_cookie("acceess")
        response.delete_cookie("refresh")
        return response

class Quiz():
    pass
    
# class UserViewSet(APIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
#     def post(self, request):
#         serializer = UserSerializer(data = request.data)
#         if serializer.is_valid():
#             user = serializer.save(request)