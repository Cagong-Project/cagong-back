from rest_framework.response import Response
from .models import User, Menu, Order
from records.models import Record
from pushQue.models import PushNotification
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post (self, request):
        # request 받기
        user_id = request.data['user_id']
        menu_id = request.data['menu_id']
        #객체를 DB에서 불러오기
        user = get_object_or_404(User, user_id=user_id)
        menu = get_object_or_404(Menu, id=menu_id)

        payment = int(menu.price)
        user_point = user.point

        if(user_point < payment):
            return Response({'message': '잔액이 부족합니다.'}, status=status.HTTP_412_PRECONDITION_FAILED)

        #user 객체의 point 차감 (user_point >= payment)
        new_point = user_point - payment
        user.point = new_point
        user.save() #DB에 유저의 갱신된 point 저장하기.
    
        timezone_now = timezone.now()

        # DB에 order 객체 추가
        order=Order(timestamp=timezone_now, customer=user, menu=menu)
        order.save()

        #DB에 record 객체 추가
        record=Record(user=user)
        record.save()

        # Notification 추가
        notification = PushNotification(user=user)
        notification.send_at = timezone_now # 처음엔 그냥 바로 입장 알림 + timezone.timedelta(hours=2)
        notification.iter = 0
        notification.title = f"CAFE {menu.cafe.name}에서 주문이 발생했습니다."
        notification.msg = f"{menu.name}을(를) 주문하셨습니다. 2시간 뒤에 다시 알려드릴게요😉"
        notification.save()

        return Response({'message': '포인트 차감, order 및 record 객체 생성 성공.', 'renewed_point':new_point}, status=status.HTTP_201_CREATED)