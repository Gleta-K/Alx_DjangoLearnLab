from django.shortcuts import render
from .models import Post

def feed_view(request):
    user = request.user
    
    # Get users the current user is following
    following_users = user.following.all()
    
    # Get posts from those users, ordered by newest first
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    return render(request, 'posts/feed.html', {'posts': posts})