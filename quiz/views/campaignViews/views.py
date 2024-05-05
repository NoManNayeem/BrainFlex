from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse
from django.contrib import messages
from django.db import IntegrityError
from quiz.models import Campaign, Participation, Quiz
import json



    
    
@login_required
@csrf_exempt
def participate(request, campaign_id):
    try:
        campaign = Campaign.objects.get(id=campaign_id)
    except Campaign.DoesNotExist:
        return render(request, 'quiz/error.html', {'error_message': 'Campaign does not exist.'})
    
    # Check if campaign status is not ONGOING
    if campaign.status != 'ONGOING':
        return render(request, 'quiz/error.html', {'error_message': f'This campaign is {campaign.status}.'})

    if request.method == 'POST':
        if Participation.objects.filter(user=request.user, campaign=campaign).exists():
            return JsonResponse({'error': 'You have already participated in this campaign.'}, status=400)

        if 'score' not in request.POST:
            return JsonResponse({'error': 'Score data missing in the request.'}, status=400)

        try:
            score = int(request.POST['score'])
            total_questions = Quiz.objects.filter(campaign=campaign).count()
            Participation.objects.create(user=request.user, campaign=campaign, score=score)
            return JsonResponse({'message': 'Score saved successfully!', 'score': score, 'total_questions': total_questions})
        except (ValueError, IntegrityError) as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        if Participation.objects.filter(user=request.user, campaign=campaign).exists():
            return render(request, 'quiz/error.html', {'error_message': 'You have already participated in this campaign.'})

        questions = Quiz.objects.filter(campaign=campaign)
        formatted_questions = []
        for question in questions:
            formatted_question = {
                'type': question.type.upper(),
                'question': question.question,
                'duration': question.duration
            }
            if question.type in ['MCQ', 'CHECKBOX']:
                formatted_question['options'] = [option.strip() for option in question.choices.split(',')]
                formatted_question['answer'] = [answer.strip() for answer in question.answer.split(',')]
            if question.type == 'IMAGE':
                formatted_question['options'] = [option.strip() for option in question.choices.split(',')]
                formatted_question['answer'] = [answer.strip() for answer in question.answer.split(',')]
                formatted_question['imageUrl'] = request.build_absolute_uri(question.image.url)
            formatted_questions.append(formatted_question)

        formatted_questions_json = json.dumps(formatted_questions)
        context = {
            'campaign': campaign,
            'questions': formatted_questions_json,
        }
        return render(request, 'quiz/campaign/participate.html', context)