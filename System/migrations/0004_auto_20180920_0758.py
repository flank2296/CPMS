# Generated by Django 2.1.1 on 2018-09-20 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0003_delete_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
