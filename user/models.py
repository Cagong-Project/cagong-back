from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, UserManager as BaseUserManager
# auth_user의 역할을 User가 대신
from django.core.validators import MinValueValidator, MaxValueValidator

#
# 커스텀 유저 모델 정의
#
class User(AbstractBaseUser):
    # 상속받아 구현한 필드
    username = models.CharField(max_length=20, unique=True, null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # 우리가 추가하는 필드
    # nickname = models.CharField(max_length=20, unique=False)
     
    #
    # customeruser필드
    #
    # TODO: 팔로워 필드
    # followers?
    point = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    #
    # owneruser 필드
    #
    cafe_id = models.CharField(max_length=50, blank=True, default="")



    # 로그인에 사용할(auth) 컬럼 지정.
    USERNAME_FIELD = 'username'
    # 필수 필드 지정
    # REQUIRED_FIELDS = ['username','nickname']

    # 프린트될 내용 세팅
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Types(models.TextChoices):
        CUSTOMERUSER = "CUSTOMERUSER"
        OWNERUSER = "OWNERUSER"

    # 디폴트는 customeruser 타입으로 세팅
    # base_type = Types.CUSTOMERUSER

    # 무슨 유저타입?
    type = models.CharField(max_length=15,
                            choices=Types.choices, default="CUSTOMERUSER")
    objects = BaseUserManager()

    # def save(self, *args, **kwargs):
    #     # if not self.id:
    #     #     self.type = self.base_type
    #     # type:"ADMINUSER" ==>
    #     # self.type = Types.ADMINUSER
    #     # type:"ADMINUSER" ==>
    #     # if User.Types.GENUSER == "GENUSER":
    #     #     self.type = self.Types.GENUSER
    #     # if self.type == "ADMINUSER":
    #     #     self.type = self.Types.ADMINUSER
    #     self.type = self.Types.CUSTOMERUSER
    #     return super().save(*args, **kwargs)

    def create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("이름 입력하셔야 합니다")
        user = self.model(
            username=username,
            password=password,
            **kwargs,
        )

        user.set_password(password)
        # user.save(using=self._db)
        user.save()
        return user

    def create_superuser(self,user_id, username, password, email, **kwargs):
        user = self.create_user(
            password=password,
            username=username,**kwargs,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        # user.save(using=self._db)
        user.save()
        return user


#
# 매니저 정의(object.all의 object)
#


class CustomerUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMERUSER)


class OwnerUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.OWNERUSER)


#
# proxy 모델 정의
#

class CustomerUser(User):
    # base_type = User.Types.CUSTOMERUSER
    objects = CustomerUserManager()    

    class Meta:
        proxy = True
        
    # 저장할 때 타입을 CUSTOMERUSER 타입으로 저장
    # def save(self, *args, **kwargs):
    #     self.type = User.Types.CUSTOMERUSER
    #     super.save(*args, **kwargs)
        
    # TODO: search_user 함수
    def search_user(keyword):
        pass
    
    # TODO: 팔로우함수
    def follow(user_id):
        pass

class OwnerUser(User):
    # base_type = User.Types.OWNERUSER
    objects = OwnerUserManager()

    class Meta:
        proxy = True
        
    # 저장할 때 타입을 OWNERUSER 타입으로 저장
    # def save(self, *args, **kwargs):
    #     self.type = User.Types.OWNERUSER
    #     super.save(*args, **kwargs)