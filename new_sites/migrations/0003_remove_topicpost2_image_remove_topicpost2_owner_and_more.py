# Generated by Django 4.1 on 2022-10-04 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_sites', '0002_topicpost2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicpost2',
            name='image',
        ),
        migrations.RemoveField(
            model_name='topicpost2',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='topicpost2',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='topicpost2',
            name='text',
        ),
    ]
