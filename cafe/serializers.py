from .models import *
from rest_framework import serializers
from user.serializers import UserSerializer

class CafeSerializer(serializers.ModelSerializer):    
    id = serializers.IntegerField()
    name = serializers.CharField()
    location = serializers.CharField()
    info = serializers.CharField()
    phone = serializers.CharField()
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Cafe
        fields = "__all__"
        

class MenuSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.CharField()
    cafe = CafeSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = "__all__"
