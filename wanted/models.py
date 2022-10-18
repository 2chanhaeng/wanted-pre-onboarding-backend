from django.db import models


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)


class Notice(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="notice")


class Application(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name="application")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="application")
