from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('quiz:login')  # Redirects to the login page or any desired URL
