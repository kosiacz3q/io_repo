from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SpierdonUser(models.Model):
    user = models.OneToOneField(User)
    level = models.IntegerField(null=False, default=0)

    def __unicode__(self):
        return self.user.__str__() + ' ' + self.level.__str__() + ' lvl'