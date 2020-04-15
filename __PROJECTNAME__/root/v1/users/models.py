# third party imports
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from root.v1.utils.models.fields import LowerEmailField


class User(AbstractUser):
    # My fields
    GENDER_FEMALE = 0
    GENDER_MALE = 1
    GENDER_OTHER = 2
    GENDER_CHOICES = [
        (GENDER_FEMALE, 'female'),
        (GENDER_MALE, 'male'),
        (GENDER_OTHER, 'other'),
    ]
    about = models.TextField(_('about'), null=True, )
    dob = models.DateField(_('date of birth'), null=True, )
    phone = models.CharField(_('phone number'), max_length=20, null=True, )
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, )
    email_verified = models.BooleanField(_('email verified'), default=False, )
    phone_verified = models.BooleanField(_('phone verified'), default=False, )
    updated_at = models.DateTimeField(_('updated at'), auto_now=True, )
    # parent class fields
    email = LowerEmailField(_('email address'), unique=True, )
    username = None
    # is_staff = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'User'

    def get_id(self):
        return self.id

    from .managers import UserQuerySet
    objects = UserQuerySet()
