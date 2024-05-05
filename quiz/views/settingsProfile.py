# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from quiz.models import Profile, Campaign, Prize

from django.contrib.auth.models import User
from django import forms
from django.contrib import messages

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'contact', 'operator', 'profile_picture']

    def save(self, user=None):
        user_profile = super().save(commit=False)
        if user:
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.save()
        user_profile.save()
        return user_profile

@login_required
def profile_page(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save(user=request.user)
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    context = {'profile': profile, 'form': form}
    return render(request, 'quiz/profile.html', context)


@login_required
def settings_page(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    context = {'profile': profile}
    return render(request, 'quiz/settings.html', context)





