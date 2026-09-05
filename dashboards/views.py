from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

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