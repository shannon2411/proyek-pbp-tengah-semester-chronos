from django import forms
from .models import Comment, Forum

class CreateDiscForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'message']

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['reply']

class UpdateDiscForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'message']
    
    def save(self, commit=True):
        form_disc = self.instance
        form_disc.title = self.cleaned_data['title']
        form_disc.message = self.cleaned_data['message']

        if commit:
            form_disc.save()
        return form_disc
