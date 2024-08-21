from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'featured_image')

        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment',
                'rows': 5,  # Corrected attribute
                'style': 'border: 2px solid #ced4da; border-radius: 0.25rem; width: 80%;'
            }),
            'featured_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border: none;'  # Make the image field borderless
            }),
        }
        