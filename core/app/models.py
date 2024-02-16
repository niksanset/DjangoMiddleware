from django.db import models
from django.contrib.auth.models import User, Group



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    



