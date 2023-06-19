from rest_framework import serializers
from .models import PushNotification


class PushNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushNotification
        fields = '__all__'


class GetNotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushNotification
        fields = ('id', 'title', 'msg', 'send_at')
