# Generated by Django 4.2 on 2023-05-27 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pushQue', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pushnotification',
            name='user_id',
        ),
        migrations.AddField(
            model_name='pushnotification',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='수신할 유저'),
        ),
    ]
