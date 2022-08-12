from django.db import models

class FamilyMember(models.Model):
    name = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    createdAt = models.DateTimeField(null=True)
