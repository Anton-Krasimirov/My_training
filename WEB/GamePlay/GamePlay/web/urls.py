from django.urls import path

from GamePlay.web.views import home_page, create_profile, dashboard, profile_details, edit_profile, delete_profile, \
    create_game, game_details, edit_game, delete_game

urlpatterns = (
    path('', home_page, name='home-page'),

    path('profile/create/', create_profile, name='create profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('game/create/', create_game, name='create game'),
    path('game/details/<int:pk>/', game_details, name='game details'),
    path('game/edit/<int:pk>/', edit_game, name='edit game'),
    path('game/delete/<int:pk>/', delete_game, name='delete game'),
)