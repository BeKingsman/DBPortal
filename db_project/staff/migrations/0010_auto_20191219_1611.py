# Generated by Django 2.2.6 on 2019-12-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_auto_20191219_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='adhaar_linked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='adhaar_no',
            field=models.IntegerField(),
        ),
    ]
