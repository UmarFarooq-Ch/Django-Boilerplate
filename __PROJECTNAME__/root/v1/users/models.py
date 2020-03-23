# third party imports
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class LowerEmailField(models.EmailField):
    """class to lower email address"""

    def get_prep_value(self, value):
        value = super(models.EmailField, self).get_prep_value(value)
        if value is not None:
            value = value.lower()
        return value


class User(AbstractUser):
    username = None
    # is_staff = None
    email = LowerEmailField(_('email address'), unique=True)
    full_name = models.CharField(_('full name'), max_length=50, null=True)
    contact_number = models.CharField(_('contact number'), max_length=20, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'User'

    def get_id(self):
        return self.id

    from .managers import UserQuerySet
    objects = UserQuerySet()
