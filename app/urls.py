from django.urls import path
from . import views


urlpatterns = [
    path('get_messages/', view=views.get_messages , name = 'get-messages'),
    path('create_message/', view=views.create_message , name = 'create-message'),
    path('authors/pro<int:author_id>/profile_picture/', view=views.update_profile_picture , name = 'update-profile-picture'),
    path('authors/<str:username>/', view=views.get_author_by_username , name = 'get-author-by-username'),
]