from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'post title',
                                                             'class': 'form-control',
                                                             }))
    content = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'post text',
                                                             'class': 'form-control',
                                                             }))


    class Meta:
        model = Post
        fields = ['title',
                  'content',
                  'img'
                  ]
