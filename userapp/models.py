from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Session_time(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.CharField(max_length=50)
    logout_time = models.CharField(max_length=50, null=True)
    ses_time = models.CharField(max_length=50, null=True)