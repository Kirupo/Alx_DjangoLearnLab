from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
            if request.user == user_to_follow:
                return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
            request.user.following.add(user_to_follow)
            return Response({"detail": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response({"detail": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
