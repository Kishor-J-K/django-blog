from .models import Category
from assignments.models import Sociallinks

def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def get_social_links(request):
    social_links = Sociallinks.objects.all()
    return {'social_links': social_links}