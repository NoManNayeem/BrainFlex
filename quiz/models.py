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



from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    STATUS_CHOICES = [
        ('ONGOING', 'Ongoing'),
        ('UPCOMING', 'Upcoming'),
        ('COMPLETED', 'Completed'),
        ('REJECTED', 'Rejected')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='winner', null=True, blank=True)
    first_runner_up = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='first_runner_up', null=True, blank=True)
    second_runner_up = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='second_runner_up', null=True, blank=True)

    def __str__(self):
        return self.name


class Prize(models.Model):
    PRIZE_CHOICES = [
        ('WINNER', 'Winner'),
        ('RUNNER_UP_1', '1st Runner Up'),
        ('RUNNER_UP_2', '2nd Runner Up')
    ]

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='prizes')
    prize_detail = models.CharField(max_length=20, choices=PRIZE_CHOICES)
    prize_description = models.TextField()

    def __str__(self):
        return f"{self.campaign.name} - {self.prize_detail}"



from django.db import models

class Quiz(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('TEXT', 'Text'),
        ('MCQ', 'Multiple Choice'),
        ('CHECKBOX', 'Checkbox')
    ]

    question = models.TextField()
    type = models.CharField(max_length=10, choices=QUESTION_TYPE_CHOICES)
    choices = models.TextField(blank=True, null=True, help_text="Enter choices separated by commas. Only required for MCQ and Checkbox type questions.")
    answer = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(default=30, help_text="Duration in seconds")

    def __str__(self):
        return self.question[:50]


from django.db import models
from django.contrib.auth.models import User

class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participations')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='participations')
    participation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'campaign')  # This ensures each user can only participate in each campaign once

    def __str__(self):
        return f"{self.user.username} - {self.campaign.name}"
