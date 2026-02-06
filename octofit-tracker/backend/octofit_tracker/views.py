from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.serializers import (
    UserSerializer,
    TeamSerializer,
    ActivitySerializer,
    LeaderboardSerializer,
    WorkoutSerializer,
)


@api_view(['GET'])
def api_root(request):
    """
    API root endpoint that lists all available endpoints.
    """
    return Response({
        'users': request.build_absolute_uri('/api/users/'),
        'teams': request.build_absolute_uri('/api/teams/'),
        'activities': request.build_absolute_uri('/api/activities/'),
        'leaderboard': request.build_absolute_uri('/api/leaderboard/'),
        'workouts': request.build_absolute_uri('/api/workouts/'),
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing teams.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing activities.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing leaderboard.
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing workouts.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
