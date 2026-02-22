from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)

            if user == request.user:
                return Response(
                    {"error": "You cannot follow yourself."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            request.user.following.add(user)

            return Response(
                {"message": "User followed successfully."},
                status=status.HTTP_200_OK
            )

        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)

            request.user.following.remove(user)

            return Response(
                {"message": "User unfollowed successfully."},
                status=status.HTTP_200_OK
            )

        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )