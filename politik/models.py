from django.db import models
from django.contrib.auth.models import User


class Politician(models.Model):
    name = models.TextField(max_length=200, blank=True)
    foreign_id = models.CharField(max_length=256, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    party = models.TextField(max_length=200, blank=True)
    fu = models.TextField(max_length=10, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    office = models.TextField(max_length=50, blank=True)
    photoURL = models.TextField(max_length=1000, blank=True)



class LawProject(models.Model):
    owner = models.OneToOneField(Politician, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=500, blank=True)
    passed = models.NullBooleanField(null=True)
    createdAt = models.DateField(null=True, blank=True)
    passedAt = models.DateField(null=True, blank=True)


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    law = models.ForeignKey(LawProject, on_delete=models.DO_NOTHING)
    vote = models.NullBooleanField(null=True)
