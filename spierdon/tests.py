from django.test import TestCase
from .models import SpierdonUser
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
        sUser.exp = 500
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
        self.assertEqual(level, 11)

    def testSpierdonGetLevelMethodPositive(self):
        """
        Check if SpierdonUser.level() method correctly handles positive value.

        :return: result of test
        """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 100
        self.assertEqual(sUser.level, 4)

    def testSpierdonGetLevelMethodZero(self):
        """
        Check if SpierdonUser.level() method correctly handles zero value.

        :return: result of test
        """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 0;
        self.assertEqual(sUser.level, 1)

    def testCalculateSpierdolUserLevel_50(self):
        """
            Check if SpierdonUser.level() method correctly handles zero value.

            :return: result of test
            """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 50
        self.assertEqual(sUser.level, 2)


    def testCalculateSpierdolUserLevel_100(self):
        """
            Check if SpierdonUser.level() method correctly handles zero value.

            :return: result of test
            """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 100
        self.assertEqual(sUser.level, 4)


    def testCalculateSpierdolUserLevel_150(self):
        """
            Check if SpierdonUser.level() method correctly handles zero value.

            :return: result of test
            """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 150
        self.assertEqual(sUser.level, 5)


    def testCalculateSpierdolUserLevel_200(self):
        """
            Check if SpierdonUser.level() method correctly handles zero value.

            :return: result of test
            """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 200
        self.assertEqual(sUser.level, 6)


    def testCalculateSpierdolUserLevel_250(self):
        """
            Check if SpierdonUser.level() method correctly handles zero value.

            :return: result of test
            """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 250
        self.assertEqual(sUser.level, 7)

    def testCalculateSpierdolUserLevel_300(self):
        """
            Check if SpierdonUser.level() method correctly handles zero value.

            :return: result of test
            """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 300
        self.assertEqual(sUser.level, 8)

    def testCalculateSpierdolUserLevel_350(self):
        """
            Check if SpierdonUser.level() method correctly handles zero value.

            :return: result of test
            """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 350
        self.assertEqual(sUser.level, 9)


    def testCalculateSpierdolUserLevel_400(self):
        """
            Check if SpierdonUser.level() method correctly handles zero value.

            :return: result of test
            """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 400
        self.assertEqual(sUser.level, 10)



    def testCalculateSpierdolUserLevel_450(self):
        """
            Check if SpierdonUser.level() method correctly handles zero value.

            :return: result of test
            """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 450
        self.assertEqual(sUser.level, 10)


    def testCalculateSpierdolUserLevel_500(self):
        """
            Check if SpierdonUser.level() method correctly handles zero value.

            :return: result of test
            """
        user = User.objects.get(username='test')
        sUser = SpierdonUser.objects.get(user=user)
        sUser.exp = 500
        self.assertEqual(sUser.level, 11)