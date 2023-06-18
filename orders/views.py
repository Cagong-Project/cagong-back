from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view

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

    # response return 할 때 갱신된 point도 같이 전달해주기.
    return Response({"message": "포인트 차감 완료!", "current_point":user.point}, status=status.HTTP_200_OK)



    # serializer = OrderSerializer(data=request.data)
    # if serializer.is_valid():
    #     # 주문 생성
    #     order = serializer.save()
        
    #     # 포인트 차감 로직
    #     point = Point.objects.get(user=request.user)
    #     point.used += order.price
    #     point.save()
        
    #     # 주문 완료 메시지 반환
    #     return Response({'message': '주문이 완료되었습니다.'}, status=201)
    
    # return Response(serializer.errors, status=400)