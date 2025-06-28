from django import forms
from django.contrib.auth.models import User
from .models import Dashboard ,Contactform
from django.core.exceptions import ValidationError



class DashboardForm(forms.ModelForm):
    # Fields from the User model
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(max_length=100)

    class Meta:
        model = Dashboard
        fields = [
            'username', 'password', 'confirm_password' ,'email',  # from User
            'register_number', 'gender', 'birthday', 'email',
            'year', 'degree_type', 'course', 'department', 'profile_photo'
        ]
        widgets = {
            'birthday': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self): # type: ignore
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise ValidationError("Passwords do not match")

    def save(self, commit=True): # type: ignore
        # Save the User first
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email =  self.cleaned_data['email'],
        )

        # Save the Dashboard (custom model)
        dashboard = super().save(commit=False)
        dashboard.user = user
        if commit:
            dashboard.save()
        return dashboard
    

class LoginForm(forms.Form):
    username = forms.CharField(label='username',max_length=100,required=True)
    password = forms.CharField(label='password',max_length=100,required=True)


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='name',max_length=100)
    email = forms.EmailField(label='email',max_length=150)
    message = forms.CharField(label='message')

    class Meta :
        model = Contactform

        fields = ['name','email','message']


from django.contrib.auth.models import User
from django import forms

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254, required=True)

    def clean_email(self):  # clean_<fieldname>
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user is registered with this email.")
        return email
    

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(label='New_Password', widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(label='Confirm_Password', widget=forms.PasswordInput, min_length=8)

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get("new_password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password
    

class DashboardUpdateForm(forms.ModelForm):
    class Meta:
       
        model = Dashboard
        fields = [
            'user',
            'register_number',
            'gender',
            'birthday',
            'email',
            'year',
            'degree_type',
            'course',
            'department',
            'profile_photo'
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta :
        model = User
        fields = [
            'username',
            'email'
        ]
        

