from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(unique=True, max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Store(models.Model):
    img = models.ImageField(upload_to='media')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    