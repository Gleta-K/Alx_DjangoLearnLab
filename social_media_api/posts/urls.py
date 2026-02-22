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