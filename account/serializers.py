
from .models import UserModel
from rest_framework import serializers
from djoser.conf import settings

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = tuple(UserModel.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
        )
        read_only_fields = (settings.LOGIN_FIELD,)