# Generated by Django 2.2.7 on 2019-11-19 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
