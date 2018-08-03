from django.db import models
from django.contrib.auth.models import User


class Politician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    office = models.TextField(max_length=50, blank=True)


class LawProject(models.Model):
    owner = models.OneToOneField(Politician, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=500, blank=True)
    passed = models.NullBooleanField(null=True)
    createdAt = models.DateField(null=True, blank=True)
    passedAt = models.DateField(null=True, blank=True)


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    law = models.ForeignKey(LawProject, on_delete=models.CASCADE)
    vote = models.NullBooleanField(null=True)
