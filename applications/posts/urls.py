from django.urls import path

from applications.posts.views import PostAPIView

urlpatterns = [
    path('', PostAPIView.as_view())
]
