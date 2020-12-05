# Third-Party Library
from rest_framework import serializers

# LocalFolder Models
from .models import PyUser


class UserSerializer(serializers.ModelSerializer):
    """Create Serializer to send User data. 
    """
    class Meta:
        model = PyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'celular', ]