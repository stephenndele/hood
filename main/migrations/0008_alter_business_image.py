# Generated by Django 3.2 on 2021-04-12 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_hood_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='image',
            field=models.URLField(default='default.png', null=True),
        ),
    ]
