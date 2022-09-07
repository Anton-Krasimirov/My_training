from django.urls import path

from Homework.mymusicapp.views import home_page, add_album, album_details, edit_album, delete_album, profile_details, \
    delete_profile, create_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('create/profile/', create_profile, name='create profile'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:id>/', album_details, name='album details'),
    path('album/edit/<int:id>/', edit_album, name='edit album'),
    path('album/delete/<int:id>/', delete_album, name='delete album'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),

)