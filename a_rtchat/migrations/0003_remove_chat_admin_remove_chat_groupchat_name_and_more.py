# Generated by Django 5.0.4 on 2024-05-07 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0002_chat_admin_chat_groupchat_name_chat_is_private_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='groupchat_name',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='is_private',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='members',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='users_online',
        ),
    ]
