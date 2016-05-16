from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from math import log, floor
from django.db.models.signals import post_save
from django.forms import ModelForm


class SpierdonUser(models.Model):
    user = models.OneToOneField(User)
    exp = models.IntegerField(null=False, default=0)
    public_level = models.BooleanField(default=False)

    @property
    def level(self):
        """
        Calculates spierdon's level based on experience value.
        """
        if self.exp < 0 and self.exp != 0:
            raise ValidationError('%(value) is less than 0', params={'value': self.exp})
        first_level_exp = 50
        try:
            if not self.exp:
                return 0
            temp = self.exp / first_level_exp
            if temp < 1:
                return 0
            temp = log(temp, 1.1)
            temp = floor(temp)
            return temp
        except:
            return 0

    def __str__(self):
        """
        Return string representation of SpierdonUser object.
        """
        return self.user.__str__() + ' ' + self.level.__str__() + ' lvl'


def create_user_profile(sender, instance, created, **kwargs):
    """
    Create SpierdonUser object associated with newly created User.
    """
    if created:
        _, _ = SpierdonUser.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)


class Challenge(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    exp = models.IntegerField(null=False, default=10)
    min_level = models.IntegerField(null=False, default=0)
    max_level = models.IntegerField(null=False, default=9999)
    picture = models.ImageField(upload_to='upload/', default='media/default.jpg')

    def __str__(self):
        """
        Return the string representation of Challenge object.
        :return:
        """
        return "%s (exp: %d)" % (self.name, self.exp)


class UserActiveChallenge(models.Model):
    challenge = models.ForeignKey(Challenge, null=False)
    user = models.ForeignKey(SpierdonUser, null=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """
        Return the string representation of UserActiveChallenge object.
        """
        return "%s %s (completed: %s)" % (self.user, self.challenge, self.completed)


class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'description', 'exp', 'min_level', 'max_level', 'picture']
