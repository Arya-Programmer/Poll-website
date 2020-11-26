from django.urls import path

from .views import PollStatDetail

StatRoutes = [
    path('<pollId>/stat/', PollStatDetail.as_view(), name="poll_stat_detail")
]