from django.db import models

# Create your models here.
from user.models import User


class Record(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.DurationField(default="00:00:00")
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(default=None, blank=True, null=True)
    memo = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.user.user_id + ' | ' + str(self.date)
