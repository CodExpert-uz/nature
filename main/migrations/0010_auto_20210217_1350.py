# Generated by Django 3.1.5 on 2021-02-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210215_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='most_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='top',
            field=models.BooleanField(default=False),
        ),
    ]
