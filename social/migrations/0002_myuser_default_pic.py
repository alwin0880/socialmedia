# Generated by Django 4.1.2 on 2022-12-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='default_pic',
            field=models.ImageField(blank=True, null=True, upload_to='defaultpic'),
        ),
    ]