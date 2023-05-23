from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Record
from .serializers import RecordSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def detail(request, record_id):
    if request.method == 'GET':
        # record = Record.objects.filter(id=record_id).first()
        records = Record.objects.all()
        print(records)
        serializer = RecordSerializer(data=records, many=True)
        if serializer.is_valid():
            return Response({"message": "디테일 겟또", "records":records}, status=status.HTTP_200_OK)
        return Response({"message": "레코드가 없습니다"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        return Response({"message": "디테일"}, status=status.HTTP_200_OK)
