# Generated by Django 4.1.2 on 2022-10-16 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wanted", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="notice",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
