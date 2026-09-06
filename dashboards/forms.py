from django import forms
from blogs.models import Category, Blog

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
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured']
        labels = {
            'title': 'Title',
            'category': 'Category',
            'featured_image': 'Featured Image',
            'short_description': 'Short Description',
            'blog_body': 'Blog Body',
            'status': 'Status',
            'is_featured': 'Is Featured',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control blog-form-input',
                'autocomplete': 'off',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ('title', 'category', 'short_description', 'blog_body'):
            self.fields[field_name].required = True
        self.fields['status'].initial = 'Draft'
        