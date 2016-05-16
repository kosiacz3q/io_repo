from django.test import TestCase
from models import SpierdonUser
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class SpierdonUserTest(TestCase):
    def setUp(self):
        """
        Initialize test.

        :return: Test user object.
        """
        user = User.objects.create_user(username="test", email="a@a.com", password="a")
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 500;
        sUser.save()

    def testSpierdonUserValues(self):
        """
        Check if SpierdonUser's properties are correct.

        :return: result of test
        """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        self.assertEqual(sUser.exp, 500)

    def testUserVulues(self):
        """
        Check if User's properties are correct.

        :return: result of test
        """
        user = User.objects.get(username='test')
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'a@a.com')

    def testSpierdonGetLevelMethod(self):
        """
        Check if SpierdonUser.level() method correctly calculate.

        :return: result of test
        """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        level = sUser.level
        self.assertEqual(level, 24)

    def testSpierdonGetLevelMethodFail(self):
        """
        Check if SpierdonUser.level() method correctly handles negative values.

        :return: result of test
        """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = -100;
        with self.assertRaises(ValidationError):
            level = sUser.level

    def testSpierdonGetLevelMethodZero(self):
        """
        Check if SpierdonUser.level() method correctly handles zero value.

        :return: result of test
        """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 0;
        self.assertEqual(sUser.level, 0)
