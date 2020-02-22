# third party imports
import django.contrib.auth.password_validation as validators
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.authtoken.models import Token as DefaultTokenModel
from rest_framework.validators import UniqueValidator

# local imports
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message='Account already exists with this email')],
        required=True
    )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'contact_number', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def validate(self, data):
        errors = dict()
        if 'password' in data:
            try:
                validators.validate_password(password=data['password'])
            except ValidationError as e:
                errors['password'] = e.messages

        if errors:
            raise serializers.ValidationError(errors)

        return data


class TokenSerializer(serializers.ModelSerializer):
    """Serializer for Token model"""

    user = UserSerializer()

    class Meta:
        model = DefaultTokenModel
        fields = ('key', 'user',)
