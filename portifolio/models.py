from django.db import models

# Create your models here.


class About_me(models.Model):
    img = models.ImageField(upload_to="about_imgs/")
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    about = models.TextField()
    html = models.IntegerField()
    css = models.IntegerField()
    javascript = models.IntegerField()
    bootstrap = models.IntegerField()
    python = models.IntegerField()
    django = models.IntegerField()
    drf = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
    
    
class MyProject(models.Model):
    img = models.ImageField(upload_to="projects/")
    project_name = models.CharField(max_length=50)
    project_link = models.CharField(max_length=150)
    project_date = models.DateTimeField()
    
    def __str__(self):
        return self.project_name
    
    
class Education(models.Model):
    img = models.ImageField(upload_to="education_imgs/")
    edu_name = models.CharField(max_length=200)
    edu_description = models.TextField()
    
    def __str__(self):
        return self.edu_name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.TextField()
    
    def __str__(self):
        return self.name