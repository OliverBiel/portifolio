from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    photo = models.ImageField(upload_to='projects')

    def __str__(self):
        return self.name