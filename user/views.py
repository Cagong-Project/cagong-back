from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer, SignupSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

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
    
class MyTokenVerifyView(TokenVerifyView):
    permission_classes = (AllowAny,)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def signin(request):
    if request.method == 'GET':
        # data = User.objects.all()
        # serializer = UserSerializer(request.user)
        # return Response(serializer.data)
        return Response( {"message": "로그인 페이지"}, status=status.HTTP_200_OK)

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
            
            login(request, user)
            return response
        # 로그인실패
        else:
            return Response({"message": "로그인에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)

# 포인트
@api_view(['GET', 'POST'])
def charge_point(request):
    if request.method == 'POST':  # POST 요청을 받은 경우
        user_id = request.data['user_id']
        user = User.objects.get(id=user_id) #DB에서 해당 id의 유저 객체

        # user_id 없음
        if user is None:
            return  Response( {"message": "존재하지 않는 아이디입니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        # 선택된 포인트와 사용자 포인트를 더한 값을 새로운 포인트로 갱신
        selected_point = request.data['selected_point']
        user_point = user.point
        print(selected_point,user_point)
        new_point = user_point + selected_point
        print(selected_point,user_point,new_point)
        
        user.point = new_point
        user.save() #DB에 유저의 갱신된 point 저장하기.

        return Response({"message": "포인트 충전 완료!", "current_point":user.point}, status=status.HTTP_200_OK)


    else:  # GET 요청을 받은 경우
        return Response({"message": "포인트 페이지"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def get_userDB(request):
    user_id = request.data['user_id']
    user = User.objects.get(id=user_id) #DB에서 해당 id의 유저 객체
    
    # user_id 없음
    if user is None:
        return  Response( {"message": "존재하지 않는 아이디입니다."}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"username":user.username, "point":user.point }, status=status.HTTP_200_OK)