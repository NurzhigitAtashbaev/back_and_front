from django.urls import path
from .views import (
    news_list_view,
    news_create_view,
    news_update_view,
    news_delete_view,
    my_api_view,
    detail_view,
)

urlpatterns = [
    path('', my_api_view),
    path('news/', news_list_view),
    path('news/detail/<int:id>/', detail_view),
    path('news/create/', news_create_view),
    path('news/update/<int:id>/', news_update_view),
    path('news/delete/<int:id>/', news_delete_view),
]