# third party imports
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# local imports
from .serializers import UserSerializer


class SignupAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        from .utils import get_token_response
        response = super().create(request, *args, **kwargs)
        return Response(data=get_token_response(user_id=response.data['id']), status=status.HTTP_201_CREATED)
