from .models import *
from rest_framework import serializers
from user.serializers import UserSerializer


class RecordSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    user = UserSerializer(read_only=True)
    start = serializers.DateTimeField()
    duration = serializers.DurationField()

    class Meta:
        model = Record
        fields = "__all__"
