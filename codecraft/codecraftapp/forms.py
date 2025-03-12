from django import forms
from .models import Application, OpenLesson
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class ApplicationForm(forms.ModelForm):
    phone = forms.CharField(
        widget=PhoneNumberPrefixWidget(
            widgets=[forms.TextInput(attrs={'class': 'form-input'})],
        )
    )

    class Meta:
        model = Application
        fields = ['fullname', 'phone', 'email', 'category']


class OpenLessonForm(forms.ModelForm):
    phone = forms.CharField(
        widget=PhoneNumberPrefixWidget(
            widgets=[forms.TextInput(attrs={'class': 'form-input'})],
        )
    )
    question = forms.CharField(widget=forms.Textarea(attrs={'col': 60, 'rows': 10}))

    class Meta:
        model = OpenLesson
        fields = ['fullname', 'phone', 'question']
