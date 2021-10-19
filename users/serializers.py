
from core.settings import USE_I18N
from django.db import models
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True
    )
    class Meta:
        model = User
        fields = "__all__"
