
  
from django.contrib.auth.models import User as UserProfile
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend


class AuthBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False


    def get_user(self, user_id):
       try:
          return UserProfile.objects.get(pk=user_id)
       except UserProfile.DoesNotExist:
          return None


    def authenticate(self, request, username, password):
        try:
            user = UserProfile.objects.get(
                Q(username=username) | Q(email=username)
            )
        except UserProfile.DoesNotExist:
            return None

        return user if user.check_password(password) else None