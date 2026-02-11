from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model."""
    list_display = ('name', 'email', 'team', 'created_at')
    list_filter = ('team', 'created_at')
    search_fields = ('name', 'email', 'team')
    ordering = ('-created_at',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model."""
    list_display = ('name', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model."""
    list_display = ('user_email', 'activity_type', 'duration', 'calories_burned', 'date', 'created_at')
    list_filter = ('activity_type', 'date', 'created_at')
    search_fields = ('user_email', 'activity_type')
    ordering = ('-date',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin interface for Leaderboard model."""
    list_display = ('user_email', 'total_calories', 'total_activities', 'rank', 'updated_at')
    list_filter = ('rank', 'updated_at')
    search_fields = ('user_email',)
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model."""
    list_display = ('name', 'difficulty', 'duration', 'calories_estimate', 'created_at')
    list_filter = ('difficulty', 'created_at')
    search_fields = ('name', 'description', 'difficulty')
    ordering = ('-created_at',)
