# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from quiz.models import Profile, Campaign, Prize

@login_required
def profile_page(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    context = {'profile': profile}
    return render(request, 'quiz/profile.html', context)

@login_required
def settings_page(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    context = {'profile': profile}
    return render(request, 'quiz/settings.html', context)

