from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from core.authentication import ExpiringTokenAuthentication


class SimpleView(APIView):
    authentication_classes = (ExpiringTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response("This is an authorized response!", status=status.HTTP_200_OK)


class ObtainExpiringAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(
                user=serializer.validated_data['user'])

            # if token already exists regenerate it
            if not created:
                token.delete()
                token = Token.objects.create(
                    user=serializer.validated_data['user'])

            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
