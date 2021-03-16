from django import forms
from .models import Tweet

MAX_TWEET_LENGTH = 240

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise forms.ValidationError('This Tweet Is Too Long!')
        return content