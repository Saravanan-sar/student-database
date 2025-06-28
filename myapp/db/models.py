from django.db import models
from django.contrib.auth.models import User

class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    register_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    birthday = models.DateTimeField()
    email = models.EmailField()
    year = models.CharField(max_length=10)
    degree_type = models.CharField(max_length=10)
    course = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def _str_(self):
        return self.user.username
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='post_images/', blank=True, null=True)


    def __str__(self):
        return self.title
    

class Contactform(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)

    def __stf__(self):
        return self.name