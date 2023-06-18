from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PushNotification
from .serializers import PushNotificationSerializer

from webpush.utils import send_to_subscription

def send_to_sub(request):
    payload = {"head": "Welcome!", "body": "Hello World"}

    user = request.user
    push_infos = user.webpush_info.select_related("subscription")
    for push_info in push_infos:
        send_to_subscription(push_info.subscription, payload)

@api_view(['GET'])
def get_push_notification(request):
    # 요청한 사용자에 할당된 푸시 알림 조회
    # (request.user와 같은 user인 푸시 알림 객체가 없는 경우, 빈 쿼리셋이 리턴됨)
    notifications = PushNotification.objects.filter(user=request.user)

    # 쿼리셋이 비어있지 않으면 (즉, 할당된 푸시 알림이 있는 경우)
    if notifications.exists():
        serializer = PushNotificationSerializer(notifications, many=True)
        data = serializer.data

        # 조회한 푸시 알림 제거
        notifications.delete()

        return Response(data, status=200)

    # 할당된 푸시 알림이 없는 경우 204 리턴, 또는 주석 처리
    return Response({'message': '푸시 알림이 없습니다.'}, status=204)

@api_view(['POST'])
def create_push_notification(request):
    serializer = PushNotificationSerializer(data=request.data)
    
    # 데이터의 유효성 판단
    if serializer.is_valid():
        notification = serializer.save()
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)