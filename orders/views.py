from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *

# 일단 기초적인 로직만 작성했음
def order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        # 주문 생성
        order = serializer.save()
        
        # 포인트 차감 로직
        point = Point.objects.get(user=request.user)
        point.used += order.price
        point.save()
        
        # 주문 완료 메시지 반환
        return Response({'message': '주문이 완료되었습니다.'}, status=201)
    
    return Response(serializer.errors, status=400)