from django.shortcuts import render

def try_now_page(request):
    return render(request, 'quiz/trial/try_now.html')  # Public landing page
