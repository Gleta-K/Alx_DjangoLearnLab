from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from .views import follow_user, unfollow_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name = "Register"),
    path('login/', LoginView.as_view(), name = "Login"),
    path('profile/', ProfileView.as_view(), name = "Profile"),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]