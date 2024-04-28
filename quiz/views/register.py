import logging
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from ..models import Profile

logger = logging.getLogger(__name__)

def register(request):
    if request.user.is_authenticated:
        return redirect('quiz:home')  # Redirect to the home page if already authenticated
    
    if request.method == 'POST':
        try:
            with transaction.atomic():
                username = request.POST.get('username')
                password = request.POST.get('password')
                email = request.POST.get('email')
                contact = request.POST.get('contact')
                operator = request.POST.get('operator')

                # Create the user
                user = User.objects.create_user(username, email, password)

                # Create the profile
                profile = Profile(user=user, contact=contact, operator=operator, email=email)
                profile.save()

                # Log in the user and redirect to the home page
                login(request, user)
                return redirect('quiz:home')
        except Exception as e:
            logger.exception("Registration failed: %s", e)
            return HttpResponseBadRequest("Registration failed. Please try again.")
    else:
        return render(request, 'quiz/register.html')  # Render the registration form
