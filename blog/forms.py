from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        widgets = {
            'title' :forms.TextInput(attrs = {'class':'form-control'}),
            'author' :forms.Select(attrs = {'class':'form-control'}),
            'body' : forms.Textarea(attrs = {'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']

        widgets = {
            'title' :forms.TextInput(attrs = {'class':'form-control'}),
            'body' : forms.Textarea(attrs = {'class':'form-control'}),
        }