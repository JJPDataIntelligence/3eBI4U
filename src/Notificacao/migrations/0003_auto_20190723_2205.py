# Generated by Django 2.1.7 on 2019-07-24 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Notificacao', '0002_auto_20190723_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='receiver_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_receiver_group', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='receiver_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_receiver_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='related_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]