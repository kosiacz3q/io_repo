from django.test import TestCase
from models import SpierdonUser
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class SpierdonUserTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="test", email="a@a.com", password="a")
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 500;
        sUser.save()



    def testSpierdonUserValues(self):
        user = User.objects.get(username = 'test')
        sUser = SpierdonUser.objects.get(user=user)
        self.assertEqual(sUser.exp, 500)

    def testUserVulues(self):
        user = User.objects.get(username='test')
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'a@a.com')

    def testSpierdonGetLevelMethod(self):
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        level = sUser.level
        self.assertEqual(level, 24)

    def testSpierdonGetLevelMethodFail(self):
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = -100;
        with self.assertRaises(ValidationError):
            level = sUser.level


    def testSpierdonGetLevelMethodZero(self):
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 0;
        self.assertEqual(sUser.level, 0)



