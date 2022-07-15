from django.db import models
from django.contrib.auth.models import AbstractUser

    
class TheUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=50,
        unique=True
    )
    REQUIRED_FIELDS = [] 
    
    def __str__(self):  
        return f"{self.first_name} {self.last_name}"
    
    
class Item(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True)
    user = models.ForeignKey(TheUser, on_delete=models.CASCADE)