# Generated by Django 2.2.6 on 2019-12-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_auto_20191220_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='Password',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
