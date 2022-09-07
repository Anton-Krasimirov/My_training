
from django import forms

from Homework.mymusicapp.models import Profile, Album


class CreatProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username",},),
            "email": forms.EmailInput(attrs={"placeholder": "Email",},),
            "age": forms.NumberInput(attrs={"placeholder": "Age",},),
        }



class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price',)
        labels = {
            'album_name': 'Album name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Descriptions',
            'image_url': 'Image URL',
            'price': 'Price',
        }
        widgets = {
            'album_name': forms.TextInput(attrs={"placeholder": 'Album name',},),
            'artist': forms.TextInput(attrs={"placeholder": 'Artist',},),
            # 'genre': forms.ChoiceField(attrs={"placeholder": '-------'},),
            'description': forms.TextInput(attrs={"placeholder": 'Descriptions',},),
            'image_url': forms.TextInput(attrs={"placeholder": 'Image URL',},),
            'price': forms.NumberInput(attrs={"placeholder": 'Price',},),
        }

class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price',)
        labels = {
            'album_name': 'Album name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Descriptions',
            'image_url': 'Image URL',
            'price': 'Price',
        }




class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price',)
        labels = {
            'album_name': 'Album name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Descriptions',
            'image_url': 'Image URL',
            'price': 'Price',
        }