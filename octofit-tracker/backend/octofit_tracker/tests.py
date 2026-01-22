from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test the User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            password="testpass123"
        )
    
    def test_user_creation(self):
        """Test user is created correctly"""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsNotNone(self.user._id)


class TeamModelTest(TestCase):
    """Test the Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )
    
    def test_team_creation(self):
        """Test team is created correctly"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(self.team.description, "A test team")
        self.assertIsNotNone(self.team._id)


class ActivityModelTest(TestCase):
    """Test the Activity model"""
    
    def setUp(self):
        from datetime import datetime
        self.activity = Activity.objects.create(
            user_id="507f1f77bcf86cd799439011",
            activity_type="Running",
            duration=30,
            calories=300,
            date=datetime.now()
        )
    
    def test_activity_creation(self):
        """Test activity is created correctly"""
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)
        self.assertIsNotNone(self.activity._id)


class LeaderboardModelTest(TestCase):
    """Test the Leaderboard model"""
    
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            team_id="507f1f77bcf86cd799439011",
            total_calories=1000,
            total_activities=10,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test leaderboard entry is created correctly"""
        self.assertEqual(self.leaderboard.total_calories, 1000)
        self.assertEqual(self.leaderboard.total_activities, 10)
        self.assertEqual(self.leaderboard.rank, 1)
        self.assertIsNotNone(self.leaderboard._id)


class WorkoutModelTest(TestCase):
    """Test the Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name="Morning Run",
            description="A refreshing morning run",
            difficulty="Medium",
            duration=45,
            calories_estimate=400,
            exercise_type="Cardio"
        )
    
    def test_workout_creation(self):
        """Test workout is created correctly"""
        self.assertEqual(self.workout.name, "Morning Run")
        self.assertEqual(self.workout.difficulty, "Medium")
        self.assertEqual(self.workout.duration, 45)
        self.assertIsNotNone(self.workout._id)


class UserAPITest(APITestCase):
    """Test the User API endpoints"""
    
    def test_get_users_list(self):
        """Test retrieving users list"""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_user(self):
        """Test creating a new user"""
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        }
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITest(APITestCase):
    """Test the Team API endpoints"""
    
    def test_get_teams_list(self):
        """Test retrieving teams list"""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_team(self):
        """Test creating a new team"""
        data = {
            'name': 'New Team',
            'description': 'A brand new team'
        }
        response = self.client.post('/api/teams/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITest(APITestCase):
    """Test the Activity API endpoints"""
    
    def test_get_activities_list(self):
        """Test retrieving activities list"""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    """Test the Leaderboard API endpoints"""
    
    def test_get_leaderboard_list(self):
        """Test retrieving leaderboard list"""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test the Workout API endpoints"""
    
    def test_get_workouts_list(self):
        """Test retrieving workouts list"""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class APIRootTest(APITestCase):
    """Test the API root endpoint"""
    
    def test_api_root(self):
        """Test API root returns all endpoints"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
