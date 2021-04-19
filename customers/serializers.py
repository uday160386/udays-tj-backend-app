from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from customers.models import User

UserModel = get_user_model()


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'password', 'confirm_password', 'gender', 'email', 'phone_number', "first_name",
            "last_name")
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                        'first_name': {'write_only': True, 'required': True},
                        'last_name': {'write_only': True, 'required': True},
                        'gender': {'write_only': True, 'required': True},
                        'confirm_password': {'write_only': True, 'required': True},
                        'email': {'write_only': True, 'required': True},
                        'phone_number': {'write_only': True, 'required': True}
                        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
