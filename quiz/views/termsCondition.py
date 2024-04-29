from django.shortcuts import render

def privacy_policy(request):
    return render(request, 'quiz/termsCondition/policies.html')

def terms_of_service(request):
    return render(request, 'quiz/termsCondition/terms.html')
