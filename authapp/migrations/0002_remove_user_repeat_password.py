# Generated by Django 4.1.3 on 2022-12-25 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='repeat_password',
        ),
    ]
