from django.test import TestCase
from .models import Profile,
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='username')
        self.user.save()

        self.profile_test = Profile(image='download.png', 
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)


class TestPost(TestCase):
    def setUp(self):
        self.profile_test = Profile(image='download.png',user=User(username='mikey'))
        self.profile_test.save()



    def test_save_image(self):
        self.image_test.save_image()

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)
