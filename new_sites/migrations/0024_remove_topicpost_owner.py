# Generated by Django 3.2 on 2021-05-02 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_sites', '0023_topicpost_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicpost',
            name='owner',
        ),
    ]
