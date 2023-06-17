from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Cafe, Menu
from .serializers import CafeSerializer, MenuSerializer
import json

@api_view(['GET'])
@permission_classes([AllowAny])
def cafelist(request):
    search_value = request.data['search_value']
     
    #DB에서 해당 값을 포함하는 카페 이름을 출력
    cafelist = list(Cafe.objects.filter(name__contains=search_value).values())
    serializer = CafeSerializer(data=cafelist, many=True)

    #is_valid() 가 에러가 난 경우 외에 검색 결과 없는 것도 확인할 수 있는건지 확인
    # 검색 결과 있음
    if serializer.is_valid():
        return Response({"message": "List of Records", "cafe_list": serializer.data}, status=status.HTTP_200_OK)

    # 검색 결과 없음
    print('에러가 났습니다 !!',serializer.errors, '데이터는 다음과 같습니다 :', serializer.data)
    return Response({"message": "invalid serializer"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def detail(request, cafe_id):
    cafe = Cafe.objects.get(id=cafe_id)
    # cafe_dict = {"name" : cafe.name, "location": cafe.location, "info": cafe.info, "phone": cafe.phone}
    # cafe_json = json.dumps(cafe_dict)

    # cafe 상세정보
    cafelist = Cafe.objects.get(id=cafe_id)
    serializer_cafe = CafeSerializer(cafelist)

    # menu 리스트
    menu = list(Menu.objects.filter(cafe = cafe_id).values())
    serializer_menu = MenuSerializer(data=menu, many= True)

    # 시리얼라이저로 front에게 전송
    if serializer_menu.is_valid():
        return Response({"message": "성공!!", "cafe_detail": serializer_cafe.data, "menu_list": serializer_menu.data}, status=status.HTTP_200_OK)
    print(serializer_menu.errors)
    return Response({"message": "유효하지 않은 serializer"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)