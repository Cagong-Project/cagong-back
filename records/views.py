from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Record
from .serializers import RecordSerializer
# Create your views here.
from django.utils import timezone


@api_view(['GET'])
def detail(request, record_id):
    record = Record.objects.filter(id=record_id).first()
    # serializer = RecordSerializer(data=record)
    # if serializer.is_valid():
    if record is not None:
        return Response({"message": "a record obj", "record":record}, status=status.HTTP_200_OK)
    return Response({"message": "레코드가 없습니다"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def done(request):
    print(request.data)
    record = Record.objects.filter(id=request.data['record_id']).first()
    print(record)
    if record is not None:
        record.end = timezone.now()  # 현재 시각으로 설정
        #record.duration = record.end - record.start  # duration 계산
        record.save()
        return Response({"message":"레코드가 업데이트 되었습니다."}, status=status.HTTP_200_OK)
    return Response({"message": "레코드가 없습니다."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def record_list(request, user_id):
    # records = 유저아이디로 검색한 레코드들을 "list of dict" 형태로 반환
    records = list(Record.objects.filter(user__user_id__contains=user_id).values())
    serializer = RecordSerializer(data=records, many= True)
    if serializer.is_valid():
        return Response({"message": "List of Records", 
                            "record_list": serializer.data}, 
                        status=status.HTTP_200_OK)
    print(serializer.errors)
    return Response({"message": "invalid serializer"}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
