from django.db import models


class Tool(models.Model):
    name = models.TextField(max_length=50)
    logo = models.ImageField(upload_to='logos')

    def __str__(self):
        return self.name