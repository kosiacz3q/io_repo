from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from math import log, floor, ceil
from django.db.models.signals import post_save
from django.forms import ModelForm


class SpierdonUser(models.Model):
    user = models.OneToOneField(User)
    exp = models.IntegerField(null=False, default=0)
    public_level = models.BooleanField(default=False)

    """
    Calculates spierdon's level based on experience value.
    """

    def compute_level(self):
        points = 0
        for level in range(1, 100):
            diff = int(level + 100 * pow(2, float(level) / 7))
            previous_points = points / 4
            points += diff
            # print("Level %d = %d" % (level + 1, points / 4))
            if points / 4 > self.exp:
                return {
                    "current": level,
                    "previous": previous_points,
                    "next": ceil(points / 4),
                }

    @property
    def level(self):
        return self.compute_level()["current"]

    @property
    def remaining(self):
        level_info = self.compute_level()
        return level_info["next"] - self.exp

    @property
    def percent(self):
        level_info = self.compute_level()
        return ceil((self.exp - level_info["previous"]) / (level_info["next"] - level_info["previous"])*100)

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
    picture = models.ImageField(upload_to='upload/', default='default.jpg')
    blocked=models.BooleanField(default=False, null=False)

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
    blocked = models.BooleanField(default=False, null=False)

    def __str__(self):
        """
        Return the string representation of UserActiveChallenge object.
        """
        return "%s %s (completed: %s)" % (self.user, self.challenge, self.completed)


class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'description', 'exp', 'min_level', 'max_level', 'picture']
