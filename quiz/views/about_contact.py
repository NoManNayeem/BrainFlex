from django.shortcuts import render, redirect
from django.core.mail import send_mail  # Required for sending emails
from django.conf import settings  # Access Django settings
from django.contrib import messages  # To display success/error messages



def about_view(request):
    return render(request, 'quiz/about.html')  # Render the 'about' template



def contact_view(request):
    if request.method == 'POST':
        # Extract form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Construct the email content
        full_message = f"Message from: {name}\nEmail: {email}\n\n{message}"

        try:
            # Send the email (configure email backend in Django settings)
            send_mail(
                subject,  # Email subject
                full_message,  # Email body
                email,  # From email address
                [settings.DEFAULT_FROM_EMAIL],  # To email address (adjust as needed)
            )
            messages.success(request, "Your message has been sent!")  # Display success message
            return redirect('quiz:contact')  # Redirect to the same page after form submission
        except Exception as e:
            messages.error(request, f"Failed to send message: {str(e)}")  # Display error message
            return redirect('quiz:contact')  # Redirect to the same page on error

    return render(request, 'quiz/contact.html')  # Render the 'contact' template
