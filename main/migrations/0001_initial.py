# Generated by Django 3.2 on 2021-04-10 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=1000)),
                ('occupants', models.CharField(max_length=500)),
                ('image', models.URLField(default='default.jpg')),
                ('health_tell', models.IntegerField(blank=True, null=True)),
                ('police_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80)),
                ('bio', models.TextField(blank=True, max_length=254)),
                ('profile_picture', models.ImageField(default='default.png', upload_to='images/')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('hood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='main.hood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hoods', to='main.profile'),
        ),
    ]
