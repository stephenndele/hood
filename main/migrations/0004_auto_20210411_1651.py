# Generated by Django 3.2 on 2021-04-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_business_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='image',
            field=models.URLField(default='default.png'),
        ),
        migrations.AlterField(
            model_name='hood',
            name='image',
            field=models.URLField(default='default.png'),
        ),
    ]
