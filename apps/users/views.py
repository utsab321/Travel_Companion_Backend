from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from apps.users.models import UserProfile
from apps.users.utils import find_similar_users
from django.views.decorators.csrf import csrf_exempt
from .models import UserLoginHistory,User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


import json



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
    })
@login_required
def profile_view(request, username):
    profile= get_object_or_404(UserProfile, user__username= username)
    return render(request, 'users/profile.html',{'profile' : profile})
# Create your views here.   
@login_required
def match_travel_buddies(request):
    profile = request.user.userprofile
    
    matches = find_similar_users(profile, limit=10, min_similarity=0.6)
    
    context = {
        'matches': [
            {
                'user': m[0].user,
                'profile': m[0],
                'similarity': m[1] * 100,  # show as percentage
            }
            for m in matches
        ],
        'your_profile': profile,
    }
    return render(request, 'users/matches.html', context)
@csrf_exempt  # Only for testing; use proper CSRF/token auth in production
def frontend_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log in user
            # Save login history
            UserLoginHistory.objects.create(
                user=user,
                ip_address=request.META.get("REMOTE_ADDR"),
                user_agent=request.META.get("HTTP_USER_AGENT")
            )
            return JsonResponse({"success": True, "message": "Logged in successfully"})
        else:
            return JsonResponse({"success": False, "message": "Invalid credentials"})
    return JsonResponse({"success": False, "message": "Only POST method allowed"})

@csrf_exempt
@csrf_exempt
def frontend_register(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Only POST allowed"}, status=405)

    try:
        # Parse JSON safely
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON"}, status=400)

        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        if not username or not password:
            return JsonResponse({"success": False, "message": "Username and password are required"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "message": "User already exists"}, status=400)

        # Create user
        user = User.objects.create_user(username=username, password=password, email=email)

        # Ensure profile is created safely
        if hasattr(user, 'userprofile'):
            user.userprofile.save()

        return JsonResponse({"success": True, "message": "Registered successfully"})

    except Exception as e:
        # Catch any server errors
        return JsonResponse({"success": False, "message": str(e)}, status=500)