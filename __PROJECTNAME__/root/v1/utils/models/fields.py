"""Custom fields for django.Model class"""

from django.db import models


class LowerEmailField(models.EmailField):
    """django model field to lower email address"""

    def get_prep_value(self, value):
        value = super(models.EmailField, self).get_prep_value(value)
        if value is not None:
            value = value.lower()
        return value
