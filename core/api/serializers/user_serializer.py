from rest_framework import serializers
from core.common.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'date_birth', 'is_active',
                  'is_admin', 'is_staff', 'date_joined', 'created_at', 'updated_at']
