from rest_framework.response import Response
from rest_framework import status
from .models import PushNotification
from .serializers import PushNotificationSerializer, GetNotiSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class get_pushNotificationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, user_id):
        # 요청한 사용자에 할당된 푸시 알림 조회
        # 유저아이디로 검색한 알림 쿼리셋을 "list of dict" 형태로 반환
        notifications =list( PushNotification.objects.filter(user__user_id__contains=user_id).values())
        
        # 쿼리셋이 비어있지 않으면 (즉, 할당된 푸시 알림이 있는 경우)
        if len(notifications):
            serializer = GetNotiSerializer(notifications, many=True)
            data = serializer.data
            # print(data)
            
            # TODO: 시간이 이미 지난 푸시 알림은 iter=9로 보냄처리
            # notifications.delete()
            
            # TODO: iter=9인 알림만 보내기

            return Response({'message': 'List of Notifications', "notifications" : data}, status=status.HTTP_200_OK)
        # 할당된 푸시 알림이 없는 경우 204 리턴, 또는 주석 처리
        return Response({'message': '푸시 알림이 없습니다.'}, status=status.HTTP_204_NO_CONTENT)

class create_pushNotificationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PushNotificationSerializer(data=request.data)
        
        # 데이터의 유효성 판단
        if serializer.is_valid():
            notification = serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)