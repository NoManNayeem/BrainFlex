from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from quiz.models import Campaign, Prize  # Import the models

@login_required
def home_page(request):
    # Fetch all campaigns
    campaigns = Campaign.objects.all()
    # Fetch prizes for all campaigns (this could be optimized if needed)
    prizes = Prize.objects.all()

    context = {
        'campaigns': campaigns,
        'prizes': prizes,
    }
    return render(request, 'quiz/home.html', context)
