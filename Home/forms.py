from django import forms
from django.forms import ModelForm, CharField, TextInput, IntegerField


class ConsumerReviewForm(forms.Form):
    review_text = forms.CharField(label='Feel free to leave a review')
