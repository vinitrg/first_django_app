from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	""" A form to edit on an existing blog or to create a new blog"""
	class Meta:
		model = Post
		fields = ('title', 'text',)