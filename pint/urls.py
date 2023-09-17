from django.urls import path
from .views import *

urlpatterns = [
    path('home/' , home , name='home/' ),
    path('home/<str:pk>/' , po_st , name='single-post' ),
    path('login/' , log_in , name='login/' ),
    path('signup/' , sign_up , name='signup/' ),
    path('logout/' , log_out , name='logout/' ),
    path('author/' , user_post , name='user-post/' ),
    path('home/<str:abc>' , owner , name='owner' ),
    path('post-upload/' , post_upload , name='post-upload/' ),
    path('edit-profile/' , edit_profile , name='edit-profile' ),
    path('explore/' , explore , name='explore' ),
    path('like/<int:post_id>/', like_post, name='like-post'),
    path('change_post_details', change_post_details, name='change_post'),
    
   


    
]
