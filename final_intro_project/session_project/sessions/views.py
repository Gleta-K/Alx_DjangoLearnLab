from django.shortcuts import render
import uuid
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.utils import timezone
from .models import UserSession
from django.utils import timezone

# Create your views here.
# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            token = str(uuid.uuid4())

            UserSession.objects.create(
                user=user,
                token=token
            )

            return JsonResponse({
                "message": "Login successful",
                "token": token
            })

        return JsonResponse({"error": "Invalid credentials"}, status=401)

    return JsonResponse({"error": "POST request required"}, status=400)

SESSION_TIMEOUT = 300  # 5 minutes

@csrf_exempt
def protected_view(request):
    token = request.headers.get("Authorization")

    if not token:
        return JsonResponse({"error": "Token required"}, status=401)

    try:
        session = UserSession.objects.get(token=token, is_active=True)
    except UserSession.DoesNotExist:
        return JsonResponse({"error": "Invalid session"}, status=401)

    time_diff = (timezone.now() - session.last_activity).total_seconds()

    if time_diff > SESSION_TIMEOUT:
        session.is_active = False
        session.save()
        return JsonResponse({"error": "Session expired"}, status=401)

    session.last_activity = timezone.now()
    session.save()

    return JsonResponse({"message": "Access granted"})

# PROTECTED
def protected_view(request):
    token = request.headers.get("Authorization")

    if not token:
        return JsonResponse({"error": "Token required"}, status=401)

    try:
        session = UserSession.objects.get(token=token, is_active=True)

        # Optional: timeout (5 minutes)
        if (timezone.now() - session.last_activity).seconds > 300:
            session.is_active = False
            session.save()
            return JsonResponse({"error": "Session expired"}, status=401)

        return JsonResponse({"message": "You accessed protected data!"})

    except UserSession.DoesNotExist:
        return JsonResponse({"error": "Invalid session"}, status=401)


# LOGOUT
def logout_view(request):
    token = request.headers.get("Authorization")

    if not token:
        return JsonResponse({"error": "Token required"}, status=401)

    try:
        session = UserSession.objects.get(token=token)
        session.is_active = False
        session.save()

        return JsonResponse({"message": "Logged out successfully"})

    except UserSession.DoesNotExist:
        return JsonResponse({"error": "Invalid session"}, status=401)
