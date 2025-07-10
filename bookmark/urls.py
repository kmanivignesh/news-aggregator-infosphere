from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_bookmark, name='add_bookmark'),
    path('list/', views.list_bookmarks, name='list_bookmarks'),
    path('bookmarks/', views.user_bookmarks, name='user_bookmarks'),
    path('bookmarks/remove/<int:bookmark_id>/', views.remove_bookmark, name='remove_bookmark'),

]
