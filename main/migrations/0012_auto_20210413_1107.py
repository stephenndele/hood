# Generated by Django 3.2 on 2021-04-13 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_business_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='main.hood'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='main.profile'),
        ),
    ]
