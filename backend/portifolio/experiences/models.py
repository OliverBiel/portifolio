from django.db import models


class Experience(models.Model):
    company = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=250)

    class Meta:
        db_table = 'experience'
        ordering = ('start_date',)

    def __str__(self):
        return self.company