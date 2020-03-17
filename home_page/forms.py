from django import forms
from home_page.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=64, required=True)
    email = forms.EmailField(max_length=64, required=True)
    phone_number = forms.CharField(max_length=32, required=True)
    message = forms.Textarea(attrs={'required': True, 'row': 4, 'cols': 10})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Your Name', 'class': 'contact_form_name input_field'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email', 'class': 'contact_form_email input_field'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Enter Phone Number', 'class': 'contact_form_phone input_field'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Input Some Message', 'class': 'text_field contact_form_message'})

    def setData(self, data):
        self.data = data
        self.is_bound = True

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 15, required = True)
    last_name = forms.CharField(max_length=15, required = True)
    email = forms.EmailField(max_length=64, required = True)
    username = forms.CharField(max_length=50, required = True)
    password = forms.CharField(widget=forms.PasswordInput())

    def setData(self, data):
        self.data = data
        self.is_bound = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter First Name', 'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter Last Name', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email', 'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter User Name', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password', 'class': 'form-control'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password']

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    def setData(self, data):
        self.data = data
        self.is_bound = True

    def authenticate(self):
        user = authenticate(username=self.data['username'], password=self.data['password'])

        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter User Name', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password', 'class': 'form-control'})

    class Meta:
        model = User
        fields = ['username', 'password']