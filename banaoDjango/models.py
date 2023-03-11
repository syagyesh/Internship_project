from django.db import models

# Create your models here.
class patient(models.Model):
    username = models.CharField(max_length=15)
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=15)
    cpassword = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.username
    
# class doctor(models.Model):
#     username = models.CharField(max_length=15)
#     firstName = models.CharField(max_length=15)
#     lastName = models.CharField(max_length=15)
#     email = models.EmailField(max_length=25)
#     password = models.CharField(max_length=15)
#     cpassword = models.CharField(max_length=15)

#     def __str__(self) -> str:
#         return self.firstName