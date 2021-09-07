from django import forms
from django.db.models import fields
from blogapp.models import *

class BlogForm(forms.ModelForm):
    class Meta():
        model = Blogpost
        fields = "__all__"