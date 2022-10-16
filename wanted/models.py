from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)


class Notice(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Application(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    notice = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
