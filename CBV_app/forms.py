from django import forms


class UserForm(forms.Form):
    
    user_name = forms.CharField(max_length=50)
    second_name = forms.CharField(max_length=50)
    nick_name = forms.CharField(max_length=50)
    age = forms.IntegerField()