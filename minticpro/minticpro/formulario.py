from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormRegistrarme(UserCreationForm):
	username = forms.CharField(label='Nombre de usuario')
	email = forms.CharField(label='Email', widget=forms.EmailInput)
	password1 = forms.CharField(label='Clave', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirme su clave', widget=forms.PasswordInput)


	class Meta:
		model = User

		fields = ['username','email','password1','password2']
		help_texts = { k:"" for k in fields }