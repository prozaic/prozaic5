# Generated by Django 3.0.6 on 2020-05-11 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_sites', '0015_topic_urllink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='urllink',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
