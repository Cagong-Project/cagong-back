from django.db import models
from user.models import User

class PushNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCAD, verbose_name="수신할 유저")  # 어떤 유저에게 보내야 할 알림인지 지정
    title = models.CharField(max_length=100)
    msg = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)  # 푸시 알림 생성 시각

    def __str__(self):
        return f"Push Title: {self.title}\nPush Message: {self.msg}"