from django.db import models

# Create your models here.
from user.models import User
import datetime


class Record(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="records")
    duration = models.DurationField(default=datetime.timedelta(0))
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(default=start, blank=True, null=True)
    memo = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{str(self.date)} | {self.user.user_id}'

    def save(self, *args, **kwargs):
        # 저장 시 자동으로 duration 필드 수정됨
        # == end 필드 업데이트 할때 자동으로 duration 필드도 업데이트됨
        self.duration = self.end - self.start 
        super(Record, self).save(*args, **kwargs)
