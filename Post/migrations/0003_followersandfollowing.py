# Generated by Django 2.2.7 on 2019-11-19 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0002_auto_20191119_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersAndFollowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('followed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to=settings.AUTH_USER_MODEL)),
                ('followed_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
