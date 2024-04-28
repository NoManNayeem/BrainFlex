from django.shortcuts import render

def landing_page(request):
    return render(request, 'quiz/landing_page.html')  # Public landing page
