# Generated by Django 2.2.5 on 2019-11-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191101_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_name',
            field=models.CharField(default='액티비티 같이 해요~!', max_length=100),
        ),
    ]
