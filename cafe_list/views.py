from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import json
from .models import Cafe

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

        print("----------------------------------------------------^^^^^^^^^^^")
        print("엥?",cafeQuerySet)
        print("----------------------------------------------------^^^^^^^^^^^")
        print(search_value, getCafeList, type(getCafeList))

        result = json.dumps(getCafeList)
        print("json 결과는", result, type(result))
        return Response({"message": "검색 성공!!!", "search_result": result}, status=status.HTTP_200_OK)
