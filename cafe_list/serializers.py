from .models import *
from rest_framework import serializers

class CafeSerializer(serializers.ModelSerializer):    
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
