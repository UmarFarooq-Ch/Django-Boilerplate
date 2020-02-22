# third party imports
from rest_framework import status
from rest_framework.authtoken.models import Token as DefaultTokenModel
from rest_framework.response import Response

# local imports
from .serializers import TokenSerializer


def get_token_response(user_id):
    """Creates a new token or gets token of user

    Arguments:
        user_id  -- id of user

    Returns:
        Response -- User object and auth token
    """
    serializer_class = TokenSerializer
    token, _ = DefaultTokenModel.objects.get_or_create(user_id=user_id)

    serializer = serializer_class(instance=token)

    return serializer.data
