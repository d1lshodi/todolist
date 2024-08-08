from django.db import models



class UserModel(models.Model):
    username = models.CharField(max_length=65, default="", unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=65, default="")
    otp  =  models.CharField(max_length=5, default="")
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.username