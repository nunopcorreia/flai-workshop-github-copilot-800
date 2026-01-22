from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'team_id', 'team_name', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_team_name(self, obj):
        if obj.team_id:
            try:
                # Convert string team_id to ObjectId for lookup
                team = Team.objects.get(_id=ObjectId(obj.team_id))
                return team.name
            except (Team.DoesNotExist, Exception):
                return None
        return None


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at']
    
    def get_id(self, obj):
        return str(obj._id)


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'user_name', 'activity_type', 'duration', 'distance', 'calories', 'date', 'notes']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user_name(self, obj):
        if obj.user_id:
            try:
                user = User.objects.get(_id=ObjectId(obj.user_id))
                return user.name
            except (User.DoesNotExist, Exception):
                return None
        return None


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'user_name', 'total_calories', 'total_activities', 'rank', 'updated_at']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user_name(self, obj):
        if obj.user_id:
            try:
                user = User.objects.get(_id=ObjectId(obj.user_id))
                return user.name
            except (User.DoesNotExist, Exception):
                return None
        return None


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'duration', 'calories_estimate', 'exercise_type']
    
    def get_id(self, obj):
        return str(obj._id)
