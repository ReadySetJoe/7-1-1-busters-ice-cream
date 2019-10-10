from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:icecream_id>/', views.detail, name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('<menu_filter>/', views.home, name='home'),
    path('<menu_filter>/upvote/<int:icecream_id>/', views.upvote, name='upvote'),
    path('<menu_filter>/downvote/<int:icecream_id>/', views.downvote, name='downvote'),
]