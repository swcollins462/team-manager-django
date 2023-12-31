from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from datetime import date
from django.core.exceptions import ValidationError
from .models import Player


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
    ('', 'feet'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
]

INCHES_CHOICES = [
    ('', 'inches'),
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


def validate_student_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))
    if 19 > age > 3:
        return birthdate
    else:
        raise ValidationError('Age must be between 4 and 18')


def validate_non_negative(num):
    if num >= 0:
        return num
    else:
        raise ValidationError('Number cannot be negative')


def validate_weight(num):
    if 25 < num < 500:
        return num
    else:
        raise ValidationError('Weight is invalid')


class AddPlayerForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control'}), label='First Name')
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control'}), label='Last Name')
    jersey_num = forms.IntegerField(required=True, validators=[validate_non_negative], widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Jersey Number', 'class': 'form-control'}), label='Number')
    position = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Position', 'class': 'form-control'}), label='Position')
    born = forms.DateField(required=True, validators=[validate_student_age], widget=forms.DateInput(
        attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}), label='Date Born')
    height_feet = forms.ChoiceField(required=True, choices=FEET_CHOICES, widget=forms.widgets.Select(
        attrs={'placeholder': 'feet', 'class': 'form-select'}), label='Height Feet')
    height_inches = forms.ChoiceField(required=True, choices=INCHES_CHOICES, widget=forms.widgets.Select(
        attrs={'placeholder': 'inches', 'class': 'form-select'}), label='Height Inches')
    weight = forms.IntegerField(required=True, validators=[validate_weight], widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Weight in Pounds', 'class': 'form-control'}), label='Weight')

    class Meta:
        model = Player
        exclude = ('user',)
