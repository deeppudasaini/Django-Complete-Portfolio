# Generated by Django 2.2.13 on 2021-06-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='./static/assets/uploads/'),
        ),
    ]
