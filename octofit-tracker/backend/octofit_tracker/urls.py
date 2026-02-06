"""
octofit_tracker app URL Configuration

This module defines URL patterns for the octofit_tracker application,
including REST API endpoints for users, teams, activities, leaderboards, and workouts.
"""
import os
from rest_framework.routers import DefaultRouter
from octofit_tracker.views import (
    UserViewSet,
    TeamViewSet,
    ActivityViewSet,
    LeaderboardViewSet,
    WorkoutViewSet,
)

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

# Determine Codespace/localhost base URL (used by validators)
codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

# Include router URLs
urlpatterns = router.urls
