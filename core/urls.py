from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from core.views import SimpleView, ObtainExpiringAuthToken

urlpatterns = [
    path('login/', ObtainExpiringAuthToken.as_view()),
    path('', SimpleView.as_view())
]
