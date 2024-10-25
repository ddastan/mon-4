from django import forms
from . models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'rate', 'category', 'tag']

    def clean_rate(self):
            rate = self.cleaned_data['rate']
            if rate > 5 or rate < 1:
                raise forms.ValidationError('Invalid rate')
            return rate


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']