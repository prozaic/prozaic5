# Generated by Django 2.2.4 on 2019-08-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_sites', '0006_entry_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]