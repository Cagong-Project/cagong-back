# Generated by Django 4.2 on 2023-05-28 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_list', '0002_cafe_phone_alter_cafe_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=6)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe_list.cafe')),
            ],
        ),
    ]
