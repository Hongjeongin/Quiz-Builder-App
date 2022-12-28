from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.translation import gettext_lazy as _

from django.shortcuts import get_object_or_404
from quiz_builder.settings import SECRET_KEY
from .serializers import UserSerializer
from .models import User

import jwt
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.exceptions import TokenError

class MyJWTAuthentication(JWTAuthentication):
        
    # Override
    def authenticate(self, request):
        print(request)
        print(request.data)
        print(request.COOKIES)
        access = request.COOKIES.get('access', None)
        refresh = request.COOKIES.get('refresh', None)
        print("asdfasdf", access, "asdfasdf")
        print(refresh, "!@#@!##!@")
        # refresh = request.COOKIES.get('refresh', None)
        # print("asdasdsadasd", refresh, "ASDASDSADSAD")
        
        # valid = get_validated_token(self, access)
        # hea
        
        if request.COOKIES == {}:
            print("none!!")
            return None
        
        if access is None:
            return None
        
        if refresh is None:
            return None
        
        validated_token = self.get_validated_token(access, refresh)
        
        return self.get_user(validated_token), validated_token
            
    # Override
    def get_validated_token(self, access, refresh):
        print("@@@@start@@@@")
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                return AuthToken(access)
            # 만료된 토큰의 경우
            except TokenError:
                try:
                    # except jwt.exceptions.ExpiredSignatureError:
                    # 1. refresh 토큰을 가지고 DB에 질의
                    # 2. if 존재한다면
                    data = {
                        "refresh": refresh
                    }
                    serializer = TokenRefreshSerializer(data = data)
                    
                    # raise_exception
                    if serializer.is_valid(raise_exception = True):
                        new_access = serializer.validated_data['access']
                        
                        # payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
                        # pk = payload.get('user_id')
                        # user = get_object_or_404(User, pk=pk)
                        # serializer = UserSerializer(instance=user)
                        # payload = jwt.decode(access, SECRET_KEY, algorithms = ['HS256'])
                        # res = Response(status = status.HTTP_200_OK)
                        # res.set_cookie('refresh', refresh)
                        # res.set_cookie('access', access)
                        return self.get_validated_token(new_access, refresh)
                    raise jwt.exceptions.InvalidTokenError
                except TokenError:
                    return Response({"message": "로그인 토큰 만료."}, status = status.HTTP_200_OK)
            
            except(jwt.exceptions.InvalidTokenError):
                return Response({"message": "로그인 만료"}, status = status.HTTP_200_OK)
    