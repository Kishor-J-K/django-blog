from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured=True).order_by('-updated_at')[:2]  # Get the latest 2 featured blogs
    context = {
        'categories': categories,
        'featured_blogs': featured_blogs
    }
    return render(request, 'home.html', context) 