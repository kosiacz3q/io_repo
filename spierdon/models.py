from django.db import models
from django.contrib.auth.models import User


class SpierdonUser(models.Model):
    user = models.OneToOneField(User)
    level = models.IntegerField(null=False, default=0)

    def __str__(self):
        """
        Returns string representation of SpierdonUser object.
        :return: string contains username and user level
        """
        return self.user.__str__() + ' ' + self.level.__str__() + ' lvl'
