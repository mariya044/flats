from django import forms
from flat.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("image","title","text","flor","all_floars","kitchen_square","all_square","living_square","price")


