from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('<int:icecream_id>/', views.detail, name='detail'),
    path('<menu_filter>/', views.index, name='index'),
    path('<menu_filter>/upvote/<int:icecream_id>/', views.upvote, name='upvote'),
    path('<menu_filter>/downvote/<int:icecream_id>/', views.downvote, name='downvote'),
]