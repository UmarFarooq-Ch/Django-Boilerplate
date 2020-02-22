# third party imports
from django.db.models.query import QuerySet
from rest_framework.generics import get_object_or_404


class UserQuerySet(QuerySet):
    def get_user_from_email(self, email):
        return get_object_or_404(self, email__iexact=email)

    def check_email(self, email):
        return self.filter(email=email).exists()
