from django.contrib import auth
from django.shortcuts import get_object_or_404, redirect, render
from assignments.models import About
from blog_main.forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from blogs.models import Category, Blog, Comment
from django.db.models import Q
from django.contrib.auth import login

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
    blog = get_object_or_404(Blog, slug=slug, status='published')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        comment_text = request.POST.get('comment', '').strip()
        if comment_text:
            Comment.objects.create(user=request.user, blog=blog, comment=comment_text)
        return redirect('blogs', slug=blog.slug)

    comments = Comment.objects.filter(blog=blog).order_by('-created_at')
    comments_count = comments.count()

    context = {
        'blog': blog,
        'comments': comments,
        'comments_count': comments_count
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


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})

    
def logout_view(request):
    auth.logout(request)
    return redirect('home')