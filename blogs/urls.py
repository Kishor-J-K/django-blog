from django.urls import path
from django.conf.urls.static import static
from blog_main import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)