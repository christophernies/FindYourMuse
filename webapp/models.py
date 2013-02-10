from django.db import models


class Person(models.Model):
	name = models.CharField(max_length=200)
	gender = models.CharField(max_length=20)
	twitter = models.CharField(max_length=200)