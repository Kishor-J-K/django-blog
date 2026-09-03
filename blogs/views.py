from django.shortcuts import redirect, render
from assignments.models import About
from blogs.models import Category, Blog
from django.db.models import Q

def home(request):
    featured_blogs = Blog.objects.filter(is_featured=True,status='published').order_by('-updated_at')[:3]  # Get the latest 3 featured blogs
    posts = Blog.objects.filter(is_featured=False, status='published').order_by('-updated_at')  # Get all non-featured blogs

    try:
        about = About.objects.get()
    except About.DoesNotExist:
        about = None

    context = {
        'featured_blogs': featured_blogs,
        'posts': posts,
        'about': about
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

def blogs(request, slug):
    try:
        blog = Blog.objects.get(slug=slug, status='published')
    except Blog.DoesNotExist:
        return redirect('home')  # Redirect to home if blog does not exist
    context = {
        'blog': blog
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    if keyword:
        posts = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword), status='published').order_by('-updated_at')
    else:
        posts = Blog.objects.none()  # Return an empty queryset if no keyword is provided

    context = {
        'posts': posts,
        'keyword': keyword
    }
    return render(request, 'search_results.html', context)