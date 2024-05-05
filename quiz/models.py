from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.db.models.signals import post_save
from django.dispatch import receiver

# Update the Profile model to use signals to save first_name and last_name
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

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
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, help_text="Upload a profile picture.")

    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except ValidationError as e:
            if 'unique' in e.message_dict.get('contact', []):
                raise ValidationError({'contact': 'This contact already exists.'})
            else:
                raise


from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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

    def clean(self):
        if self.start_date and self.end_date and self.start_date >= self.end_date:
            raise ValidationError("End date must be after start date.")

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
from django.conf import settings

class Quiz(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('TEXT', 'Text'),
        ('MCQ', 'Multiple Choice'),
        ('CHECKBOX', 'Checkbox'),
        ('IMAGE', 'Image')
    ]
    
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    question = models.TextField()
    type = models.CharField(max_length=10, choices=QUESTION_TYPE_CHOICES)
    choices = models.TextField(blank=True, null=True, help_text="Enter choices separated by commas. Only required for MCQ and Checkbox type questions.")
    answer = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(default=30, help_text="Duration in seconds")
    image = models.ImageField(upload_to='quiz_images/', blank=True, null=True, help_text="Upload an image for the question. Only required for Image type questions.")

    def __str__(self):
        return self.question[:50]
    
    def get_image_url(self):
        if self.image:
            return f"{settings.MEDIA_URL}{self.image}"
        else:
            return None



from django.db import models
from django.contrib.auth.models import User

class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participations')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='participations')
    participation_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'campaign')  # This ensures each user can only participate in each campaign once

    def __str__(self):
        return f"{self.user.username} - {self.campaign.name}"

