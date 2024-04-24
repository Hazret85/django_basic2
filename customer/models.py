from django.db import models

class CustomerProfile(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    experience = models.TextField()

    def __str__(self):
        return self.name
