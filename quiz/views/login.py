from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=username, password=password)  # Correct call
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('quiz:home')  # Redirect to home page
        else:
            form = AuthenticationForm()  # Re-initialize the form if invalid

    return render(request, 'quiz/login.html', {'form': form})
