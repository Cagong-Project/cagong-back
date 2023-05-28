from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Cafe, Menu
from .serializers import CafeSerializer, MenuSerializer
import json
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def cafelist(request):
    if request.method == 'POST':  # GET 요청을 받은 경우
        search_value = request.data['search_value']
        # cafe = Cafe.objects.filter(name=search_value).first() #DB에서 해당 값을 포함하는 카페 이름을 출력

        cafeQuerySet = Cafe.objects.filter(name__contains=search_value)
        # 검색 결과 없음
        if cafeQuerySet is None:
            return  Response( {"message": "결과가 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
 
        # 검색 결과 있음
        getCafeList = Cafe.cafeToDictionary(cafeQuerySet) #dictionary 형태
        result = json.dumps(getCafeList)
        print("json 결과는", result, type(result))
        return Response({"message": "검색 성공!!!", "search_result": result}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def menu(request, cafe_id):
    cafe = Cafe.objects.get(id=cafe_id)
    cafe_dict = {"name" : cafe.name, "location": cafe.location, "info": cafe.info, "phone": cafe.phone}
    cafe_json = json.dumps(cafe_dict)

    menu = list(Menu.objects.filter(cafe = cafe_id).values())
    serializer_menu = MenuSerializer(data=menu, many= True)

    # 시리얼라이저로 front에게 전송
    if serializer_menu.is_valid():
        return Response({"message": "성공!!", "cafe_detail": cafe_json, "menu_list": serializer_menu.data}, status=status.HTTP_200_OK)
    print(serializer_menu.errors)
    return Response({"message": "유효하지않은 serializer"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)