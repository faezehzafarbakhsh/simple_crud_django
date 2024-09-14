from django.db import models


class GenderEnum(models.TextChoices):
    FEMALE = 'female', 'Female'
    MALE = 'male', 'Male'


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=6,
        choices=GenderEnum.choices,
        default=GenderEnum.MALE
    )
    birth_date = models.DateField(null=True, blank=True)
    degree_level = models.CharField(max_length=50, null=True, blank=True)
    enrollment_date = models.DateTimeField(null=True, blank=True)
    graduation_date = models.DateTimeField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
