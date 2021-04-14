from django.db import models

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)


class StudentInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    dob = models.DateField(null=True)
    grade = models.CharField(max_length=1)
    schoollastattend = models.CharField(max_length=100)
    address = models.TextField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
