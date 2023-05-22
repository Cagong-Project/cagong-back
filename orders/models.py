from django.db import models
from django.conf import settings

# 카페 모델
class Cafe(models.Model):
    location = models.CharField(max_length=255, verbose_name="카페 주소")
    phone = models.CharField(max_length=20, verbose_name="카페 전화번호")

    def __str__(self):
        return self.location

# 메뉴 목록 모델
class Category(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=255, verbose_name="카테고리명")

    def __str__(self):
        return self.name

# 메뉴 (상품 1개) 모델
class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menus')
    name = models.CharField(max_length=255, verbose_name="상품명")
    price = models.IntegerField(verbose_name="가격")
    image = models.ImageField(upload_to='menu_images', verbose_name="이미지")

    def __str__(self):
        return self.name

# 포인트 모델
class Point(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE, 
                             verbose_name="사용자")
    amount = models.IntegerField(verbose_name="포인트 총량")
    used = models.IntegerField(verbose_name="사용된 포인트")

    def __str__(self):
        return f"{self.user.username} - {self.amount}"

# 주문 모델
class Order(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="주문 시각")
    orderer = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, 
                                verbose_name="주문자")
    price = models.IntegerField(verbose_name="가격")
    cafe_name = models.CharField(max_length=255, verbose_name="카페명")
    product = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name="상품")

    def __str__(self):
        return f"Order #{self.pk}"