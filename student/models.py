from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
# Create your models here.

class Student(models.Model):
    studentID = models.AutoField(primary_key=True)
    studentNumber = models.CharField(max_length=10)
    studentName = models.CharField(max_length=100)
    facultyName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username