from rest_framework import serializers
from .models import *

# class CafeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cafe
#         fields = '__all__'
        
# class MenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         fields = '__all__'

# class PointSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Point
#         fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'