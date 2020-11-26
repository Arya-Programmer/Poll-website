from django.urls import path
from .views import PollDetail

PollRoutes = [
    path('<pollId>/', PollDetail.as_view(), name="poll_detail")
]