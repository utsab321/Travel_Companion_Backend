from django.urls import path,include
from .views_api import match_users
from .views import get_current_user
from . import views_api
from .import views
urlpatterns = [
    path("api/login/", views.frontend_login, name="frontend-login"),
    path("api/register/", views.frontend_register, name="frontend-register"),  
    path("api/matches/", match_users),
    path('api/match/<int:match_id>/action/', views_api.MatchActionView.as_view(), name='match-action'),
    path('users/me/', get_current_user),
    path('api/kyc/', include('apps.kyc.urls')),

]