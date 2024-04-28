from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

def login_view(request):
    if request.user.is_authenticated:
        return redirect('quiz:home')  # Redirect to the home page if already authenticated
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username, password)
        if user:
            login(request, user)  # Log in the user
            return redirect('quiz:home')  # Redirect to the home page
        else:
            return HttpResponseBadRequest("Invalid credentials. Please try again.")

    return render(request, 'quiz/login.html')  # Render the login form
