from tkinter import Widget
from django import forms
from django.contrib.auth import password_validation
from antique.models import Evaluation, VerificationCode, CustomUser

class VerificationCodeForm(forms.ModelForm):
    code = forms.CharField(label='code', help_text='enter SMS verification Number')
    class Meta:
        model = VerificationCode
        fields = ('code',)

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username', help_text='username')
    email = forms.CharField(label='Email', help_text='email')
    password = forms.CharField(
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'password', 'username', 'email']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_validation.validate_password(password, self.instance)
        return password
class EvaluationRequestForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)
    contact_method = forms.ChoiceField(choices=[('phone', 'Phone'), ('email', 'Email')])
    class Meta:
        model = Evaluation
        fields = ['comment', 'contact_method', 'antique_img']
    
    def clean_photo(self):
        antique_img = self.cleaned_data.get('antique_img')

        # Check if a photo is provided
        if not antique_img:
            raise forms.ValidationError("Please upload a photo.")

        # Check the file size 5 MB
        max_size = 5 * 1024 * 1024  
        if antique_img.size > max_size:
            raise forms.ValidationError("File size must be no more than 5 MB.")
        return antique_img