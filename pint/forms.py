from django import forms
from .models import *

class UserData(forms.ModelForm):
    class Meta:
        model = post
        fields = ['image', 'title', 'desc' ]
        
              
class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture' , 'bio' ]

class EditPost(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title' , 'desc' ]
        
              
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        
class Change_post(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'desc']
    

