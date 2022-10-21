from django.forms import ModelForm
from homepage.models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['username', 'feedback']
