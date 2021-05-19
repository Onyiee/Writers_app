from django import forms
from .models import Tweet


class NewTweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = "__all__"


