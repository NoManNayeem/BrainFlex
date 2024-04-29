# Inside your quiz/views.py file

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from quiz.models import Campaign  # Ensure you have the Campaign model imported

@login_required
def campaign_detail_view(request):
    # Render the participate.html template with campaign context
    return render(request, 'quiz/campaign/participate.html')
