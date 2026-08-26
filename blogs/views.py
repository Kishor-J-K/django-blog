from django.shortcuts import redirect, render
from blogs.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured=True,status='published').order_by('-updated_at')[:3]  # Get the latest 3 featured blogs
    posts = Blog.objects.filter(is_featured=False, status='published').order_by('-updated_at')  # Get all non-featured blogs
    context = {
        'categories': categories,
        'featured_blogs': featured_blogs,
        'posts': posts
    }
    return render(request, 'home.html', context) 

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category_id=category_id, status='published').order_by('-updated_at')
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return redirect('home')  # Redirect to home if category does not exist
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'posts_by_category.html', context)