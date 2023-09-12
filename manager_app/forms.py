from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Player
from django.db.models.fields import BLANK_CHOICE_DASH


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length='50', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}),)
    last_name = forms.CharField(label='Last Name', max_length='50', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}),)
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}),)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


FEET_CHOICES = [
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
]

INCHES_CHOICES = [
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
]


class AddPlayerForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control'}), label='First Name')
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control'}), label='Last Name')
    jersey_num = forms.IntegerField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Jersey Number', 'class': 'form-control'}), label='Jersey Number')
    position = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Position', 'class': 'form-control'}), label='Position')
    born = forms.DateField(required=True, widget=forms.DateInput(
        attrs={'class': 'form-control'}), label='Date Born')
    height_feet = forms.ChoiceField(required=True, choices=BLANK_CHOICE_DASH + FEET_CHOICES, widget=forms.widgets.Select(
        attrs={'placeholder': 'feet', 'class': 'form-control'}), label='Height Feet')
    height_inches = forms.ChoiceField(required=True, choices=BLANK_CHOICE_DASH + INCHES_CHOICES, widget=forms.widgets.Select(
        attrs={'placeholder': 'inches', 'class': 'form-control'}), label='Height Inches')
    weight = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Weight in Pounds', 'class': 'form-control'}), label='Weight in Pounds')

    class Meta:
        model = Player
        exclude = ('user',)
