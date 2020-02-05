from django.urls import path
from . import views

urlpatterns = [
    path('loggedout/', views.loggedout, name='loggedout'),

# urls for main tabs
    path('', views.main, name='main'),
    path('post/list/', views.post_list, name='post_list'),
    path('contacts/', views.contacts, name='contacts'),

# urls for dance style pages
    path('breakdance/', views.breakdance, name='breakdance'),
    path('contemporary/', views.contemporary, name='contemporary'),
    path('hiphop/', views.hiphop, name='hiphop'),
    path('aerial_silks/', views.aerial_silks, name='aerial_silks'),
    path('detskaya_horeografiya/', views.detskaya_horeografiya, name='detskaya_horeografiya'),
    path('modern/', views.modern, name='modern'),
    path('jazzfunk/', views.jazzfunk, name='jazzfunk'),
    path('latina/', views.latina, name='latina'),

# urls for posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
