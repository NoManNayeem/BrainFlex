from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse
from django.contrib import messages
from django.db import IntegrityError
from quiz.models import Campaign, Participation, Quiz
import json




@login_required  # Apply login_required decorator
@csrf_exempt
def participate(request, campaign_id):
    try:
        campaign = Campaign.objects.get(id=campaign_id)
    except Campaign.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'Campaign does not exist.'})

    if request.method == 'POST':
        # Check if the user has already participated in the campaign
        if Participation.objects.filter(user=request.user, campaign=campaign).exists():
            return JsonResponse({'error': 'You have already participated in this campaign.'}, status=400)

        # Check if the request has the 'score' data
        if 'score' not in request.POST:
            return JsonResponse({'error': 'Score data missing in the request.'}, status=400)

        try:
            # Get the score and total questions from the request data
            score = int(request.POST['score'])
            total_questions = Quiz.objects.filter(campaign=campaign).count()

            # Save the participation record
            Participation.objects.create(user=request.user, campaign=campaign, score=score)

            # Return a success response
            return JsonResponse({'message': 'Score saved successfully!', 'score': score, 'total_questions': total_questions})
        except (ValueError, IntegrityError) as e:
            # Handle errors when parsing score or saving participation
            return JsonResponse({'error': str(e)}, status=400)

    else:
        # Check if the user has already participated in the campaign
        if Participation.objects.filter(user=request.user, campaign=campaign).exists():
            return render(request, 'quiz/error.html', {'error_message': 'You have already participated in this campaign.'})

        # Fetch questions for the campaign
        questions = Quiz.objects.filter(campaign=campaign)

        # Prepare questions data in the required format
        formatted_questions = []
        for question in questions:
            formatted_question = {
                'type': question.type.upper(),  # Ensure type is uppercase
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

        # Serialize formatted_questions to JSON
        formatted_questions_json = json.dumps(formatted_questions)

        context = {
            'campaign': campaign,
            'questions': formatted_questions_json,
        }

        return render(request, 'quiz/campaign/participate.html', context)