from django import forms
from .models import Book , Category

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ('created_at','user', 'slug',)

class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ('created_at','user', 'slug',)
class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)

