# Generated by Django 2.2.4 on 2019-08-15 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_sites', '0003_topic_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/pdfs/')),
            ],
        ),
    ]
