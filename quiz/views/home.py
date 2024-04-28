from django.shortcuts import render

def home_page(request):
    # Your logic for rendering the landing page goes here
    return render(request, 'quiz/home.html')
