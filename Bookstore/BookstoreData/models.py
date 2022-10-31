from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

    
    
class Books(models.Model):
    Author = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    publish_date = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)