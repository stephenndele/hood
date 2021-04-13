from django.test import TestCase
from .models import Profile,Hood,Business, Post
from django.contrib.auth.models import User
class ProfileTestClass(TestCase):
    from django.contrib.auth.models import User
    def setUp(self):
        self.user = User(username='stephen')
        self.user.save()
        self.profile = Profile(profile_picture='default.png',bio='My name is Stephen', name='person')
        self.profile.save_profile()
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Hood.objects.all().delete()
        Business.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.profile, Profile))
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)


class HoodTestClass(TestCase):
    def setUp(self):
        self.hood = Hood(name='Yes', location='Nairobi',
        image='default.png', 
        occupants='0',
        health_tell='0', 
        police_number='0')
        self.hood.save_hood()
 
    def test_create_hood(self):
        self.hood.save_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_hood(self):
        self.hood.save_hood()
        self.hood.delete_hood()
        hoods = Hood.objects.all()
        hood = Hood.search_hood('test')
        self.assertTrue(len(hoods) <= 0)

    def test_update_hood(self):
        self.hood.save_hood()
 

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business = Business(name='Yes',
        image='default.png', 
        email='busines@gmsil.com',
        description='we love business',)
        self.business.create_business()

    def test_delete_business(self):
        self.business.create_business()
        self.business.delete_business()
        posts = Business.objects.all()
        self.assertTrue(len(posts) <= 0)
    def search_business(self):
        self.business.create_business()
        post = Business.find_business(business_id)
        self.assertEqual(post.id,'1')

class TestPost(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='mimi')
        self.post = Post.objects.create(title='title', post='post', date='date')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_update_post(self):
        self.post.update_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_create_posts(self):
        self.post.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_post('test')
        self.assertTrue(len(post) < 1)