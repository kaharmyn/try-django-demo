from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"\"{title}\" is already in use. Please pick another title.")
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    '''
    Raw input = dirty
    Django forms clean this data (preventing scripting attacks)
    Cleaned data = savable or usable.
    '''

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        return cleaned_data
