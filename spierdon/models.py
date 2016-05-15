from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from math import log, floor
import os

class SpierdonUser(models.Model):
    user = models.OneToOneField(User)
    # level = models.IntegerField(null=False, default=0)
    exp = models.IntegerField(null=False, default=0)

    def get_level(self):
        if self.exp < 0:
            raise ValidationError(
                ('%(value) is less than 0'),
                params={'value': self.exp}
            )
        first_level_exp = 50
        temp = self.exp / first_level_exp
        temp = log(temp, 1.1)
        temp = floor(temp)
        return temp

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
    min_level = models.IntegerField(null=False, default=0)
    max_level = models.IntegerField(null=False, default=9999)
    picture = models.ImageField(upload_to='spierdon/', default='spierdom/challenge.jpg')


    def __str__(self):
        return "%s (exp: %d)" % (self.name, self.exp)
