from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm,AuthenticationForm
#from django.contrib.auth.models import User
from django import forms
from myblog.models import Profile
from django.contrib.auth import get_user_model
from .models import OTP

User = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter emailid'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['password'].label = ''
class ProfilePageForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label='First Name (required)')
    last_name = forms.CharField(max_length=30, required=False, label='Last Name')

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'profile_pic', 'web_url', 'facebook_url', 'instagram_url', 'twitter_url', 'github_url', 'linkedin_url')
        labels = {
            'bio': 'Add your Bio (required)',
            'profile_pic': 'Add your profile picture:',
            'web_url': 'Add your website:',
            'facebook_url': 'Add your Facebook account:',
            'instagram_url': 'Add your Instagram account:',
            'twitter_url': 'Add your Twitter account:',
            'github_url': 'Add your GitHub account:',
            'linkedin_url': 'Add your LinkedIn account:',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'placeholder': 'Add your bio here'}),
            'web_url': forms.TextInput(attrs={'placeholder': 'http://www.example.com'}),
            'facebook_url': forms.TextInput(attrs={'placeholder': 'http://facebook.com/user_name'}),
            'instagram_url': forms.TextInput(attrs={'placeholder': 'http://instagram.com/user_name'}),
            'twitter_url': forms.TextInput(attrs={'placeholder': 'http://twitter.com/user_name'}),
            'github_url': forms.TextInput(attrs={'placeholder': 'http://github.com/user_name'}),
            'linkedin_url': forms.TextInput(attrs={'placeholder': 'http://linkedin.com/user_name'}),
        }

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data.get('last_name', '')
        if commit:
            user.save()
            profile.save()
        return profile

class EditProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'web_url', 'facebook_url', 'instagram_url', 'twitter_url', 'github_url', 'linkedin_url')
        labels = {
            'bio': 'Add your Bio (required)',
            'profile_pic': 'Add your profile picture:',
            'web_url': 'Add your website:',
            'facebook_url': 'Add your Facebook account:',
            'instagram_url': 'Add your Instagram account:',
            'twitter_url': 'Add your Twitter account:',
            'github_url': 'Add your GitHub account:',
            'linkedin_url': 'Add your LinkedIn account:',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'placeholder': 'Add your bio here'}),
            'web_url': forms.TextInput(attrs={'placeholder': 'http://www.example.com'}),
            'facebook_url': forms.TextInput(attrs={'placeholder': 'http://facebook.com/user_name'}),
            'instagram_url': forms.TextInput(attrs={'placeholder': 'http://instagram.com/user_name'}),
            'twitter_url': forms.TextInput(attrs={'placeholder': 'http://twitter.com/user_name'}),
            'github_url': forms.TextInput(attrs={'placeholder': 'http://github.com/user_name'}),
            'linkedin_url': forms.TextInput(attrs={'placeholder': 'http://linkedin.com/user_name'}),
        }


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email','username','password1','password2']
        labels = {
            'email':'Enter mail Id',
            'username':'Enter Username',
            'password1':'Enter Password',
            'password2':'Enter Password again'
        }
        widgets = {
       ' email' : forms.EmailInput(attrs={'placeholder':'Enter email id','label':''}),
        'username' : forms.TextInput(attrs={'placeholder':'Enter username','label':''}),
        'password1' : forms.PasswordInput(attrs={'placeholder':'Enter Password','label':''}),
        'password2' : forms.PasswordInput(attrs={'placeholder':'Re-enter Password','label':''}),
        }

class OtpForm(forms.ModelForm):
    class Meta:
        model = OTP
        fields = ['otp','email']
        widgets = {
            'otp' : forms.TextInput(attrs={'placeholder':'Enter OTP','label':''}),
            'email' : forms.EmailInput(attrs={'type':'hidden'})
        }
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'example@mail.com'}))
    first_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'placeholder':'elijah'}))
    last_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'placeholder':'Mikaelson'}),required=False)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']



class PasswordChangingForm(PasswordChangeForm):
    old_password =  forms.CharField(widget=forms.PasswordInput(attrs={'type':'password'}))
    new_password1 = forms.CharField(max_length = 100,widget=forms.PasswordInput(attrs={'type':'password'}))
    new_password2 = forms.CharField(max_length = 100,widget=forms.PasswordInput(attrs={'type':'password'}))

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
