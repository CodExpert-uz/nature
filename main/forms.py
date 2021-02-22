from django.forms import ModelForm,Textarea
from .models import Register


class JoinUsForm(ModelForm):
	""" Join us form to Register model """
	class Meta:
		model = Register
		fields = ('name','email','course','message')
		widgets = {
			'message': Textarea(attrs={'cols': 30, 'rows': 8}),
		}