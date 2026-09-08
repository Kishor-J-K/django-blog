from django import forms 
from blogs.models import Category, Blog 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

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
        
        
class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name','is_staff', 'is_active','is_superuser','groups','user_permissions']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'password': 'Password',
            'is_staff': 'Staff Status',
            'is_active': 'Active Status',
            'is_superuser': 'Superuser Status',
            'groups': 'Groups',
        } 
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control user-form-input',
                'autocomplete': 'off',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control user-form-input',
                'autocomplete': 'off',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control user-form-input',
                'autocomplete': 'off',
            }),
        }
        