from django.db import models
from django.contrib.auth.models import User

# User model is here---

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    portfolio_site = models.URLField(blank=True)
    
    def __str__(self):
        return self.user.username
