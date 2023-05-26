from django.db import models

class PushNotification(models.Model):
    title = models.CharField(max_length=100)
    msg = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)  # 푸시 알림 생성 시각
