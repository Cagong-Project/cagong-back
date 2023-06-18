from rest_framework import serializers
from .models import *
from user.serializers import UserSerializer
from cafe.serializers import MenuSerializer


class OrderSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField()
    customer = UserSerializer(read_only=True)
    menu = MenuSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'