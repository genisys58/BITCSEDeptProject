# Generated by Django 2.0.2 on 2018-02-12 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSE_Department', '0008_auto_20180211_1337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('user',)},
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='dummy', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='1234567890', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
