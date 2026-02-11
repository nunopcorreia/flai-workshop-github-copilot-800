from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'first_name', 'last_name', 'email', 'team', 'created_at']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else str(obj.pk) if obj.pk else None


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else str(obj.pk) if obj.pk else None


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_email', 'activity_type', 'duration', 'distance', 'calories_burned', 'date', 'created_at']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else str(obj.pk) if obj.pk else None
    
    def get_user(self, obj):
        try:
            user = User.objects.get(email=obj.user_email)
            return user.name
        except User.DoesNotExist:
            return obj.user_email


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_email', 'team', 'total_points', 'total_calories', 'total_activities', 'rank', 'updated_at']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else str(obj.pk) if obj.pk else None
    
    def get_user(self, obj):
        try:
            user = User.objects.get(email=obj.user_email)
            return user.name
        except User.DoesNotExist:
            return obj.user_email
    
    def get_team(self, obj):
        try:
            user = User.objects.get(email=obj.user_email)
            return user.team if user.team else 'No Team'
        except User.DoesNotExist:
            return 'No Team'


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'duration', 'calories_estimate', 'created_at']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else str(obj.pk) if obj.pk else None
