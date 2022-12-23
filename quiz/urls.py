from django.urls import (
    path,
    include
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.routers import DefaultRouter

from . import views
from .serializers import MyTokenObtainPairView

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename = 'user')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name = 'token_verify'),  

    
    
    # path('login/'),
    # path('register/', ),
    # path('')
]