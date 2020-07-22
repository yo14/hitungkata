from django.contrib import admin
from django.urls import path
from basic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('count/', views.count, name='count'),
    path('whatthis/', views.whatthis, name='whatthis'),
]
