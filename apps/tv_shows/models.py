from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) <= 2:
            errors["title"] = "Title should be at least two characters"
        if len(postData['network']) <= 3:
            errors["network"] = "Network should be at least three characters"
        if len(postData['description']) <= 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"Show object: ({self.id}) {self.title} {self.network} {self.release_date}"

# Create your models here.
