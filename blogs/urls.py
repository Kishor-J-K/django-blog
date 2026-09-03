from django.urls import path
from django.conf.urls.static import static
from blog_main import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('search/', views.search, name='search'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('<slug:slug>/', views.blogs, name='blogs'),        
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)