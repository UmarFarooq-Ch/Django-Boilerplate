from django.contrib.auth.models import UserManager


class UserQuerySet(UserManager):

    # function override to handle username==None
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        if username:
            extra_fields['username'] = self.model.normalize_username(username)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # function override to handle username==None
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)

    # function override to handle username==None
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        return super().create_superuser(username, email, password, **extra_fields)

    def get_user_from_email(self, email):
        from rest_framework.generics import get_object_or_404
        return get_object_or_404(self, email__iexact=email)

    def check_email(self, email):
        return self.filter(email=email).exists()
