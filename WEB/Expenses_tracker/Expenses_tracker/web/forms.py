import os
from django import forms

from Expenses_tracker.web.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'budget': 'Budget',
            'profile_image': 'Profile Image',
        }