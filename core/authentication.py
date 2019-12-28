from django.utils.timezone import now
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.conf import settings


class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        self.model = self.get_model()
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid Token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        if token.created < now() - settings.EXPIRING_TOKEN_LIFESPAN:
            raise exceptions.AuthenticationFailed('Token has expired')

        return (token.user, token)
