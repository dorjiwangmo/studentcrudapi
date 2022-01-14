from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=100, blank=True)
    lname = models.CharField(max_length=100, blank=True)
    std_id = models.CharField(max_length=10, blank=True)
    contact_no = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.std_id
