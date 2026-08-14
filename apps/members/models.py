from django.db import models

class Member(models.Model):
    DEPARTMENT_CHOICES = [
        ('teacher', 'Teacher'),
        ('administration', 'Administration'),
        ('staff', 'Staff'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    occupation = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='members/')
    is_local = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
