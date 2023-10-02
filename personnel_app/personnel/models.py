from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Personnel(models.Model):

    TITLE = (
        (1, 'Team Lead'),
        (2, 'Mid Lead'),
        (3, 'Junior'),
    )

    GENDER = (
        (1, 'Female'),
        (2, 'Male')
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.PositiveSmallIntegerField(choices=TITLE, default=1)
    gender = models.PositiveSmallIntegerField(choices=GENDER, default=1)
    salary = models.PositiveIntegerField(blank=True)
    department = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Departments(models.Model):
    name = models.ForeignKey(Personnel, related_name='department', on_delete=models.CASCADE)