from django.urls import path

from Expenses_tracker.web.views import home_page, create_expense, edit_expense, delete_expense, profile_edit, \
    delete_profile, show_profile, create_profile

urlpatterns = (
    path('', home_page, name='home page'),

    path("create/", create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/', show_profile, name='show profile'),
    path('profile/edit/', profile_edit, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

)
