from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from quiz.models import Campaign, Participation, Quiz
import json

def participate(request, campaign_id):
    try:
        campaign = Campaign.objects.get(id=campaign_id)
    except Campaign.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'Campaign does not exist.'})

    if request.method == 'POST':
        # Handle form submission
        # Process submitted answers
        # Calculate score and save participation record
        return redirect('result_page')  # Replace 'result_page' with the URL name of the result page
    else:
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
                formatted_question['imageUrl'] = question.image.url
            formatted_questions.append(formatted_question)

        # Serialize formatted_questions to JSON
        formatted_questions_json = json.dumps(formatted_questions)

        context = {
            'campaign': campaign,
            'questions': formatted_questions_json,
        }
        return render(request, 'quiz/campaign/participate.html', context)
