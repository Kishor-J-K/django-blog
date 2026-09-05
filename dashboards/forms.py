from django import forms

from blogs.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        labels = {
            'category_name': 'Category name',
        }
        widgets = {
            'category_name': forms.TextInput(attrs={
                'class': 'form-control category-form-input',
                'autocomplete': 'off',
            }),
        }