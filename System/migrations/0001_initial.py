# Generated by Django 2.1.1 on 2018-09-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('pin', models.CharField(max_length=6)),
                ('ssc', models.CharField(max_length=4)),
                ('hsc', models.CharField(max_length=4)),
                ('ug', models.CharField(max_length=4)),
                ('pg', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=10)),
                ('middle_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'register',
            },
        ),
    ]
