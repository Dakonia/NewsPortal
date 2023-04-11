from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            # 'author',
            'categoryType',
            'tittle',
            'text',
            'postCategory'
        ]



    def clean_tittle(self):
        tittle = self.cleaned_data["tittle"]
        if tittle[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return tittle

    def clean_text(self):
        text = self.cleaned_data["text"]
        if text[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return text