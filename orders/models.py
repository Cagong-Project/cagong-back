from django.db import models
from django.conf import settings
from user.models import User
from cafe.models import Menu

# 주문 모델
class Order(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="주문 시각")
    customer = models.ForeignKey(User, 
                                on_delete=models.CASCADE, 
                                verbose_name="주문자")
    # payment = models.IntegerField(verbose_name="지불 금액")  # 필요가 없을 것 같음. 그냥 그만큼 차감되면 되니까.
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name="상품")

    def __str__(self):
        return f"Order #{self.pk}"