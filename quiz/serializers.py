from rest_framework import serializers
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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

class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only = True)
    email = serializers.EmailField(required = True, allow_blank = False, max_length = 128)
    password = serializers.CharField(write_only = True, style = {'input_type': 'password'})
    validation = serializers.BooleanField(required = False)
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'registered_date', 'validation']
    
    # if user exist, raise error message
    def validate(self, data):
        email = data.get('email', None)
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError("user already exsits")
        
        return data