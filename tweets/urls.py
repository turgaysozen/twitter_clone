from django.urls import path
from .views import (tweet_list_drf_serializer, 
                          tweet_detail, 
                          create_tweet_django_forms, 
                          create_tweet_drf_serializer, 
                          tweet_detail_view_drf_serializer,
                          tweet_delete_drf,
                          tweet_action_drf)

urlpatterns = [
    path('', tweet_list_drf_serializer),
    path('action', tweet_action_drf),
    path('<int:tweet_id>', tweet_detail_view_drf_serializer),
    path('create', create_tweet_drf_serializer),
    path('<int:tweet_id>/delete', tweet_delete_drf),
]
