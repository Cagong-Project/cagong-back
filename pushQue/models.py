from django.db import models
from user.models import User
# from django.utils import timezone

class PushNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="수신할 유저", null=True)  # 어떤 유저에게 보내야 할 알림인지 지정
    title = models.CharField(max_length=100)
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 푸시 알림 생성 시각

    iter = models.IntegerField(default=0)
    send_at = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.title}\n | {self.msg}"