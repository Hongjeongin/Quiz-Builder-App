from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User, Quiz, Question, Solution, Solved_quiz

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)  
        return token
    
    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        
        refresh = self.get_token(self.user)
        
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['success'] = True
        
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only = True)
    email = serializers.EmailField(required = True, allow_blank = False, max_length = 128)
    password = serializers.CharField(required = True, write_only = True, style = {'input_type': 'password'})
    validation = serializers.BooleanField(required = False)
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'registered_date', 'validation']    