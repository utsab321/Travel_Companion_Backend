from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import find_similar_users
from .models import Match,UserProfile
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def match_users(request):
    try:
        profile = request.user.userprofile
    except  UserProfile.DoesNotExist:
        return Response({"detail": "User profile not found"}, status=404)
    matches = find_similar_users(profile)

    result = []

    for user, similarity in matches:

        result.append({
            "username": user.user.username,
            "similarity": similarity
        })

    return Response(result)
class MatchActionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, match_id):
        match = get_object_or_404(Match, id=match_id)

        # Security: only the receiver can accept/reject
        if match.user2 != request.user:
            return Response({"detail": "Not authorized"}, status=403)

        action = request.data.get("action").lower() # "accept" or "reject"

        if action == "accept":
            match.status = "accepted"
            match.save()
            # Optional: create reverse match or chat room here
            return Response({"status": "accepted"})

        elif action == "reject":
            match.status = "rejected"
            match.save()
            return Response({"status": "rejected"})

        return Response({"detail": "Invalid action"}, status=400)