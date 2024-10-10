from django import forms
from django.forms import ModelForm
from .models import Post,Category,Comment
from tinymce.widgets import TinyMCE


choices = Category.objects.all().values_list('name','name')
choice_list = [item for item in choices]
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','body','header_image')
        labels = {
            'title':'',
            'body':'',
            'category':'',
            'header_image':'Upload image here'
        }
        widgets = {
            'title' : forms.TextInput(attrs={'placeholder':'Title of Blog'}),
            'author' : forms.TextInput(attrs={'value':'','type':'hidden','id':'author_field'}),
            'category' : forms.Select(choices=choice_list), 
            'body': TinyMCE(attrs={'cols': 60, 'rows': 30}),
        }


class EditForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','body','header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'placeholder':'Title of Blog'}),
            'body' : forms.Textarea(attrs={'class':'form-control bg-dark text-light'}),
        }



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control ','placeholder':'Name','id':'comment_name'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name':'',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'Category',"onkeyup":"this.value = this.value.toLowerCase();"}),
        }