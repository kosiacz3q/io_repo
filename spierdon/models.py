from django.db import models
from django.contrib.auth.models import User


class SpierdonUser(models.Model):
    user = models.OneToOneField(User)
    # level = models.IntegerField(null=False, default=0)
    exp = models.IntegerField(null=False, default=0)

    def get_level(self):
        return null

    def __str__(self):
        """
        Returns string representation of SpierdonUser object.
        :return: string contains username and user level
        """
        return self.user.__str__() + ' ' + self.level.__str__() + ' lvl'


class Challenge(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    exp = models.IntegerField(null=False, default=10)

    def __str__(self):
        return "%s (exp: %d)" % (self.name, self.exp)
