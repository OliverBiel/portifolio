from django.db import models


class Academic(models.Model):
    institution = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    description = models.CharField(max_length=250)

    class Meta:
        db_table = 'academic'
        ordering = ('start_date',)

    def __str__(self):
        return self.institution