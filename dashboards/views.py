from django.shortcuts import get_object_or_404, redirect, render 
from blogs.models import Category, Blog 
from django.contrib.auth.decorators import login_required 
from .forms import CategoryForm, BlogForm 
from django.contrib.auth.models import User 
from .forms import AddUserForm

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count
    }
    return render(request, 'dashboards/dashboard.html', context)

# Categories CRED operations

@login_required(login_url='login')
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'dashboards/categories.html', context)


@login_required(login_url='login')
def add_category(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('categories')

    return render(request, 'dashboards/add_category.html', {'form': form})


@login_required(login_url='login')
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    form = CategoryForm(request.POST or None, instance=category)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('categories')

    return render(request, 'dashboards/edit_category.html', {'form': form, 'category': category})


@login_required(login_url='login')
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
    return redirect('categories')

# Posts CRED operations

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboards/posts.html', context)

@login_required(login_url='login')
def add_post(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts')

    context = {
        'form': form,
    }
    return render(request, 'dashboards/add_post.html', context)

def edit_post(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    form = BlogForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('posts')

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboards/edit_post.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    if request.method == 'POST':
        post.delete()
    return redirect('posts')


# Users CRED operations 

@login_required(login_url='login')
def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboards/users.html', context)

def add_user(request):
    form = AddUserForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('users')
    return render(request, 'dashboards/add_user.html', {'form': form})

@login_required(login_url='login')
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = AddUserForm(request.POST or None, instance=user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('users')
    return render(request, 'dashboards/edit_user.html', {'form': form, 'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
    return redirect('users')