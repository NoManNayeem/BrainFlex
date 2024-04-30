from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from quiz.models import Campaign, Prize, Participation  # Import the models

@login_required
def home_page(request):
    # Fetch campaigns that the user has not participated in
    user_participated_campaigns = Participation.objects.filter(user=request.user).values_list('campaign', flat=True)
    campaigns = Campaign.objects.exclude(id__in=user_participated_campaigns)

    # Fetch prizes for all campaigns (this could be optimized if needed)
    prizes = Prize.objects.all()

    context = {
        'campaigns': campaigns,
        'prizes': prizes,
    }
    return render(request, 'quiz/home.html', context)
