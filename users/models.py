from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.forms import ValidationError
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class UserInfo(models.Model):
    username = models.CharField(max_length=25, null=False, blank=False, unique=True, validators=[
    RegexValidator(r'^[a-zA-Z0-9_]+$', message='Username must contain only letters or numbers and underscores.'), MinLengthValidator(4)])
    email = models.EmailField(max_length=30, validators=[MinLengthValidator(5)], null=False,blank=False, unique=True)
    phone = models.CharField(max_length=12, validators=[MinLengthValidator(10)], null=True, blank=True, unique=True)
    password = models.CharField(max_length=256, null=False,blank=False,validators=[MinLengthValidator(4)])
    class Meta:
        db_table = 'userinfo'
    
    def save(self, *args, **kwargs):
        if not self.id:  
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def validate_password_strength(value):
        if len(value) < 4:
            raise ValidationError('Password must be at least 4 characters long.')
    password = models.CharField(max_length=256, validators=[validate_password_strength])
    
