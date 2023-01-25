from django import forms

from social.models import MyUser,Posts,Storys
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control border-dark'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control border-dark'}))
    class Meta():
        model=MyUser
        fields=['first_name','last_name','username','email',
        'phone','profile_pic','password1','password2']
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control border-dark'}),
            "last_name":forms.TextInput(attrs={'class':'form-control border-dark'}),
            "username":forms.TextInput(attrs={'class':'form-control border-dark'}),
            "email":forms.EmailInput(attrs={'class':'form-control border-dark'}),
            "phone":forms.NumberInput(attrs={'class':'form-control border-dark'}),
            "profile_pic":forms.FileInput(attrs={'class':'form-select border-dark'})
        }



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","Placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","Placeholder":"password"}))


class AddPostForm(forms.ModelForm):
    class Meta():
        model=Posts
        fields=['image','location','description']


class AddStoryForm(forms.ModelForm):
    class Meta():
        model=Storys
        fields=['story']
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=MyUser
        fields=['first_name','last_name','username','email',
        'phone','Bio']   
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control'}),
            "last_name":forms.TextInput(attrs={'class':'form-control'}),
            "username":forms.TextInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
            "phone":forms.NumberInput(attrs={'class':'form-control'}),
            "Bio":forms.Textarea(attrs={'class':'form-control','rows':'2'})

        }
        