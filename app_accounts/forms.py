from django import forms
from . import models


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.Accounts
        fields = ['username', 'age', 'profile_picture', 'bio', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class EditMyProfileForm(forms.ModelForm):
    class Meta:
        model = models.Accounts
        fields = ['username', 'age', 'bio', 'profile_picture', 'password']
