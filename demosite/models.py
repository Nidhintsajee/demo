from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    email = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.user.username)
