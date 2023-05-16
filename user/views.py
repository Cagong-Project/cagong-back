from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer, SignupSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import check_password
# from rest_framework.views import APIView

# from django.contrib.auth import authenticate, login, logout


@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET', 'POST'])
def signin(request):
    # 임시
    # signin_serializer = SigninSerializer(data=request.data)
    # # user_id 존재
    # if signin_serializer.is_valid():
    #     pass
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        user_id = request.data['user_id']
        password = request.data['password']
        user = User.objects.filter(user_id=user_id).first()
        
        # user_id 없음    
        if user is None:
            return  Response( {"message": "존재하지 않는 아이디입니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        # 비밀번호 틀림
        if not check_password(password, user.password):
            return Response( {"message": "비밀번호가 틀렸습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        # user 가 맞다면,
        if user is not None:
            token = MyTokenObtainPairSerializer.get_token(user) # refresh 토큰 생성
            refresh_token = str(token)
            access_token = str(token.access_token)
            response = Response({
                        "user": UserSerializer(user).data,
                        "message": "login success",
                        "jwt_token": {
                            "access_token": access_token,
                            "refresh_token": refresh_token
                        },
                    }, status=status.HTTP_200_OK)
            response.set_cookie("access_token", access_token, httponly=True)
            response.set_cookie("refresh_token", refresh_token, httponly=True)
            return response
        # 로그인실패
        else:
            return Response({"message": "로그인에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)