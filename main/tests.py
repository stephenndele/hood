from django.test import TestCase

from django.test import TestCase
import datetime as dt
from django.contrib.auth.models import User
from .models import Hood, Business, Post, Profile

# Create your tests here.

class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.stephen= User(first_name = 'stephen', last_name ='ndele', password = 'test1234', email ='stephen@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.stephen,User))


    # Testing Save Method
    def test_save_method(self):
        self.stephen.save()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)


class HoodTestClass(TestCase):

    def setUp(self):
        # Creating a new user and saving it
        self.stephen= User(first_name = 'stephen', last_name ='ndele', email ='stephen@gmail.com')
        self.stephen.save_User()

        

        self.new_hood= Hood(title = 'Test Hood',body = 'This is a random test Hood',user = self.stephen)
        self.new_hood.save()


    def tearDown(self):
        User.objects.all().delete()
        Hood.objects.all().delete()

class PostTestClass(TestCase):

    def setUp(self):
        # Creating a new user 
        self.stephen= User(first_name = 'stephen', last_name ='ndele', email ='stephen@gmail.com')
        self.stephen.save_User()

        

        self.new_post= Post(title = 'Test Post',body = 'This is a random test Post',user = self.stephen)
        self.new_post.save()


    def tearDown(self):
        User.objects.all().delete()
        Post.objects.all().delete()


class BusinessTestClass(TestCase):

    def setUp(self):
        # Creating a new user 
        self.stephen= User(first_name = 'stephen', last_name ='ndele', email ='stephen@gmail.com')
        self.stephen.save_User()

        

        self.new_business= Business(title = 'Test Business',body = 'This is a random test Business',user = self.stephen)
        self.new_business.save()


    def tearDown(self):
        User.objects.all().delete()
        Business.objects.all().delete()

