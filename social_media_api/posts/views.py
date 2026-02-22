from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import Post, Like
from notifications.models import Notification


class PostFeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if Like.objects.filter(user=request.user, post=post).exists():
            return Response(
                {"detail": "You already liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )

        Like.objects.create(user=request.user, post=post)

        # Create notification
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                content_type=ContentType.objects.get_for_model(post),
                object_id=post.id,
            )

        return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)
    
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        like = Like.objects.filter(user=request.user, post=post)

        if not like.exists():
            return Response(
                {"detail": "You have not liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )

        like.delete()
        return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)    