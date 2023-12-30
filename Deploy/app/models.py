from email.policy import default
from django.db import models

# Create your models here.
class UserImageModel(models.Model):
    image = models.ImageField(upload_to = 'images/')
    type1 = models.CharField(max_length=20,default='data')
    print('type',type(type1))

    def __str__(self):
        return str(self.image),str(self.type1)

class DoctorFeedModel(models.Model):
    Feedback = models.TextField(max_length=100)

    def __str__(self):
        return str(self.Feedback)