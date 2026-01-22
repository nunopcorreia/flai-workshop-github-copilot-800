from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model"""
    list_display = ('name', 'email', 'team_id', 'created_at')
    list_filter = ('created_at', 'team_id')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('User Information', {
            'fields': ('name', 'email', 'password')
        }),
        ('Team Assignment', {
            'fields': ('team_id',)
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model"""
    list_display = ('name', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Team Information', {
            'fields': ('name', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model"""
    list_display = ('activity_type', 'user_id', 'duration', 'distance', 'calories', 'date')
    list_filter = ('activity_type', 'date')
    search_fields = ('activity_type', 'user_id', 'notes')
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Activity Details', {
            'fields': ('user_id', 'activity_type', 'duration', 'distance', 'calories', 'date')
        }),
        ('Additional Information', {
            'fields': ('notes',)
        }),
    )


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin interface for Leaderboard model"""
    list_display = ('user_id', 'rank', 'total_calories', 'total_activities', 'updated_at')
    list_filter = ('rank', 'updated_at')
    search_fields = ('user_id',)
    readonly_fields = ('updated_at',)
    ordering = ('rank',)
    
    fieldsets = (
        ('User Information', {
            'fields': ('user_id',)
        }),
        ('Statistics', {
            'fields': ('total_calories', 'total_activities', 'rank')
        }),
        ('Timestamps', {
            'fields': ('updated_at',)
        }),
    )


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model"""
    list_display = ('name', 'exercise_type', 'difficulty', 'duration', 'calories_estimate')
    list_filter = ('difficulty', 'exercise_type')
    search_fields = ('name', 'description', 'exercise_type')
    
    fieldsets = (
        ('Workout Information', {
            'fields': ('name', 'description', 'exercise_type')
        }),
        ('Workout Details', {
            'fields': ('difficulty', 'duration', 'calories_estimate')
        }),
    )
