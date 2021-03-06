from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image

# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=1000)
    occupants = models.CharField(max_length=500)
    image = models.URLField(
        default='https://sharingtheglobe.files.wordpress.com/2012/02/dsc_0290.jpg')
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hoods', null=True)
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} hood'

    def create_hood(self):
        self.save()
        
    def save_hood(self):
        self.save()


    def delete_hood(self):
        self.delete()

    def update_hood(self):
        self.update()

    @classmethod
    def search_hood(cls, name):
        return cls.objects.filter(name__icontains=name).all()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png', null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    hood = models.ForeignKey(Hood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} profile'


    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
    

    @receiver(post_save, sender=User)
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()
class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(
        default='default.png', null=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='business', null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner', null=True)

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()


class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner', null=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='hood_post', null=True)

    def __str__(self):
        return f'{self.name} Post'

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def save_post(self):
        self.save()

    def update_post(self):
        self.save()
    
    @classmethod
    def search_post(cls, title):
        return cls.objects.filter(title__icontains=title).all()