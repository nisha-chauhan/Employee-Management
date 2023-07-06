from django import forms
from .models import Feedback

# class FeedbackForm(forms.Form):
#     email=forms.EmailField(label="Enter your email", max_length=100)
#     rating=forms.IntegerField(label="Enter your rating",max_length=1)
#     feedback=forms.CharField(label="Your feedback",widget=forms.Textarea)
    
# def __init__(self, *args, **kwargs):
#         super(FeedbackForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
            
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['email','rating','feedback']