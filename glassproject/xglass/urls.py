
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
        path('', views.home, name='home'),
        path('contact/', views.contact, name='contact'),
        path('about/', views.about, name='about'),
        path('prodect/', views.glass_product, name='glass_product'),
        path('all_product/<int:pk>', views.all_product, name='all_product'),
        path('category/<str:foo>', views.category, name='category'),
       







]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


