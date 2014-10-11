from django import forms
 
class HashtagForm(forms.Form):
    hashtag = forms.CharField(max_length=10, required = True)
