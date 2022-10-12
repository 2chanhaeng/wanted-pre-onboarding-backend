from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateTimeField()


class User(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateTimeField()


class Notice(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateTimeField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Application(models.Model):
    date = models.DateTimeField()
    notice = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
