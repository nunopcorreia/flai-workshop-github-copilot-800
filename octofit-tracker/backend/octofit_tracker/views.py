from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer,
    TeamSerializer,
    ActivitySerializer,
    LeaderboardSerializer,
    WorkoutSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing User operations.
    Provides list, create, retrieve, update, and destroy actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Team operations.
    Provides list, create, retrieve, update, and destroy actions.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Activity operations.
    Provides list, create, retrieve, update, and destroy actions.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Leaderboard operations.
    Provides list, create, retrieve, update, and destroy actions.
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Workout operations.
    Provides list, create, retrieve, update, and destroy actions.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
