# Generated by Django 2.2.13 on 2021-06-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_work_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='date',
        ),
        migrations.AddField(
            model_name='work',
            name='endtime',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='starttime',
            field=models.DateField(null=True),
        ),
    ]
