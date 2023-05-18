from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    # response 커스텀 
    default_error_messages = {
        'no_active_account': {'message':'username or password is incorrect!',
                              'success': False,
                              'status' : 401}
    }
    # 유효성 검사
    def validate(self, attrs):
        data = super().validate(attrs)
        
        refresh = self.get_token(self.user)
        
         # response에 추가하고 싶은 key값들 추가
        data['username'] = self.user.username
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['success'] = True
        
        return data