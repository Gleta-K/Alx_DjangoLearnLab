from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import feed

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

from django.urls import path

urlpatterns += [
    path('feed/', feed, name='user-feed'),
]

from django.urls import path
from .views import LikePostView, UnlikePostView

urlpatterns = [
    path("posts/<int:pk>/like/", LikePostView.as_view(), name="like-post"),
    path("posts/<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike-post"),
]