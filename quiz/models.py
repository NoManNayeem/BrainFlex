from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    contact = models.CharField(max_length=13, unique=True)
    OPERATOR_CHOICES = (
        ('GP', 'GrameenPhone'),
        ('BL', 'Banglalink'),
        ('RB', 'Robi'),
        ('TT', 'Teletalk'),
    )
    operator = models.CharField(max_length=2, choices=OPERATOR_CHOICES)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
