from django import forms
from .models import UserImageModel, DoctorFeedModel

class UserImageForm(forms.ModelForm):
    class Meta():
        model = UserImageModel
        fields = ['image']

class DoctorFeedForm(forms.ModelForm):
    class Meta():
        model = DoctorFeedModel
        fields = '__all__'