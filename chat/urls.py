from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.message_page,name='home'),
    path('create-profile/',views.create_profile,name='profile'),
    path('all-profiles/',views.show_all_profiles,name='all-profiles'),
    # path('profile/edit/',views.edit_profile,name='edit-profile'),
    path('send-message/<profile_id>/',views.send_message,name='send-message'),
    path('register/',views.register,name='register'),

    path('logout/',views.logout_user,name='logout'),

]