from django import forms
from wanted.models import Company, User


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name"]
