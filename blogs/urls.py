from django.urls import path
from django.conf.urls.static import static
from blog_main import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)