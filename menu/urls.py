from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:icecream_id>/', views.detail, name='detail'),
    path('featured/', views.featured, name='featured'),
    path('daily/', views.daily, name='daily'),
    path('weekly/', views.weekly, name='weekly'),
    path('seasonal/',views.seasonal, name='seasonal'),
]