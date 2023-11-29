from django import forms
from django.contrib.auth import password_validation
from antique.models import VerificationCode, CustomUser

class VerificationCodeForm(forms.ModelForm):
    code = forms.CharField(label='code', help_text='enter SMS verification Number')
    class Meta:
        model = VerificationCode
        fields = ('code',)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_validation.validate_password(password, self.instance)
        return password
class EvaluationRequestForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    contact_method = forms.ChoiceField(choices=[('phone', 'Phone'), ('email', 'Email')])