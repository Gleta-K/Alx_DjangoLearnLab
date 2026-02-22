from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from .views import FollowUserView, UnfollowUserView
urlpatterns = [
    path('register/', RegisterView.as_view(), name = "Register"),
    path('login/', LoginView.as_view(), name = "Login"),
    path('profile/', ProfileView.as_view(), name = "Profile"),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user')
]