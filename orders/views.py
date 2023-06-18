from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import OrderSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.utils import timezone

@api_view(['POST'])
def order(request):

    # request 받기
    user_id = request.data['user_id']
    menu_id = request.data['menu_id']

    #객체를 DB에서 불러오기
    user = User.objects.get(id=user_id)
    menu = Menu.objects.get(id=menu_id)

    #user 객체의 point 차감 (일단 point가 충분히 있다는 가정하에)
    payment = int(menu.price)
    user_point = user.point
    new_point = user_point - payment
    user.point = new_point
    user.save() #DB에 유저의 갱신된 point 저장하기.


    # DB에 order 객체 저장 성공 (serializer 사용 안 하긴 함.)
    order=Order(timestamp=timezone.now(), customer=user, menu=menu)
    order.save()

    return Response({'message': '포인트 차감, 주문 객체 생성 성공적.'}, status=status.HTTP_201_CREATED)