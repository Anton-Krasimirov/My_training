import os
from django import forms

from Expenses_tracker.web.models import Profile, Expense


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

class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Link to Image',
            'price': 'Price',
        }

class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ()
        labels = {

        }