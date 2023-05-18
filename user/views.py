from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer, SignupSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import check_password

from django.contrib.auth import login, logout


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.method == 'GET':
        # data = User.objects.all()
        # serializer = UserSerializer(
        #     data, context={'request': request}, many=True)
        # return Response(serializer.data)
        return Response( {"message": "회원가입페이지"}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 완료!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def signin(request):
    if request.method == 'GET':
        # data = User.objects.all()
        # serializer = UserSerializer(request.user)
        # return Response(serializer.data)
        return Response( {"message": "로그인 페이지"}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        
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
            
            login(request, user)
            return response
        # 로그인실패
        else:
            return Response({"message": "로그인에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)