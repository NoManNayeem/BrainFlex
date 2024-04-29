from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('quiz:home')  # Ensure this URL name is correctly configured in your URLconf.
            else:
                form.add_error(None, 'Invalid username or password')
        # No else needed here as form is passed to the template with errors
    else:
        form = AuthenticationForm()  # Only initialize a new form if it's not a POST request.

    return render(request, 'quiz/login.html', {'form': form})
