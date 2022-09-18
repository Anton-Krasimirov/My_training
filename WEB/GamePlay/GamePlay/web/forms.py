import os

from django import forms

from GamePlay.web.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,)

    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        labels = {'email': 'Email', 'age': 'Age', 'password': 'Password', }


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


# class DeleteProfile(forms.ModelForm):
#
#     def save(self, commit=True):
#
#         image_path = self.instance.profile_picture.path
#         self.instance.delete()
#         Game.objects.all().delete()
#
#         os.remove(image_path)
#         return self.instance
#
#     class Meta:
#         model = Profile
#         fields = ()


class CreateGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class EditGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class DeleteGame(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = '__all__'