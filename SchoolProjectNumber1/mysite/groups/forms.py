from django import forms
from .models import Group


class PostForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['profiles',
                  'group_name',
                  'group_description',
                  'img'
                  ]
