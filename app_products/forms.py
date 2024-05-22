from django.forms import ModelForm, CharField, PasswordInput
from app_accounts.models import Accounts
from . import models


class EditProfileForm(ModelForm):
    password = CharField(widget=PasswordInput)

    class Meta:
        model = Accounts
        fields = ['username', 'age', 'bio', 'password', 'profile_picture']


class AddProductForm(ModelForm):
    class Meta:
        model = models.Products
        fields = ['category', 'name', 'description', 'price', 'image']


class EditProductForm(ModelForm):
    class Meta:
        model = models.Products
        fields = ['category', 'name', 'description', 'price', 'image']


class AddCommentForm(ModelForm):
    class Meta:
        model = models.Comments
        fields = ['comment']


class EditCommentForm(ModelForm):
    class Meta:
        model = models.Comments
        fields = ['comment']
