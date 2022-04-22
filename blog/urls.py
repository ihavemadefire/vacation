from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<slug:slug>/', views.post_detail, name='detail'),
    path('dogs/', views.all_dogs, name='all_dogs'),
    path('dog/<int:pk>', views.one_dog, name='one_dog'),
    path('dog/create/', views.create_dog, name='create_dog'),
    path('dog/update/<int:pk>', views.update_dog, name='update_dog'),
    path('owners/', views.all_owners, name='all_owners'),
    path('owner/<int:pk>', views.one_owner, name='one_owner'),
    path('owner/create/', views.create_owner, name='create_owner'),
    path('owner/update/<int:pk>', views.update_owner, name='update_owner'),
]