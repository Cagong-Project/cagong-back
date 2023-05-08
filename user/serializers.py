from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = "__all__"

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
    def create(self, validated_data):
        user = User.objects.create_user(
            user_id=validated_data['user_id'],
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            phone=validated_data['phone'],
            type=validated_data['type'],
            #TODO: follower 추가
        )
        return user