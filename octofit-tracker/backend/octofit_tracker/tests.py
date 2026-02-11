from django.test import TestCase
from django.utils import timezone
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Tests for the User model."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create(
            name="John Doe",
            email="john@example.com",
            team="Team Alpha"
        )

    def test_user_creation(self):
        """Test that a user can be created."""
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.team, "Team Alpha")
        self.assertIsNotNone(self.user.created_at)

    def test_user_string_representation(self):
        """Test the string representation of a user."""
        self.assertEqual(str(self.user), "John Doe")


class TeamModelTest(TestCase):
    """Tests for the Team model."""

    def setUp(self):
        """Set up test data."""
        self.team = Team.objects.create(
            name="Team Alpha",
            description="The best team in the competition"
        )

    def test_team_creation(self):
        """Test that a team can be created."""
        self.assertEqual(self.team.name, "Team Alpha")
        self.assertEqual(self.team.description, "The best team in the competition")
        self.assertIsNotNone(self.team.created_at)

    def test_team_string_representation(self):
        """Test the string representation of a team."""
        self.assertEqual(str(self.team), "Team Alpha")


class ActivityModelTest(TestCase):
    """Tests for the Activity model."""

    def setUp(self):
        """Set up test data."""
        self.activity = Activity.objects.create(
            user_email="john@example.com",
            activity_type="Running",
            duration=30,
            calories_burned=250,
            date=timezone.now()
        )

    def test_activity_creation(self):
        """Test that an activity can be created."""
        self.assertEqual(self.activity.user_email, "john@example.com")
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories_burned, 250)
        self.assertIsNotNone(self.activity.date)
        self.assertIsNotNone(self.activity.created_at)

    def test_activity_string_representation(self):
        """Test the string representation of an activity."""
        self.assertEqual(str(self.activity), "john@example.com - Running")


class LeaderboardModelTest(TestCase):
    """Tests for the Leaderboard model."""

    def setUp(self):
        """Set up test data."""
        self.leaderboard_entry = Leaderboard.objects.create(
            user_email="john@example.com",
            total_calories=1500,
            total_activities=10,
            rank=1
        )

    def test_leaderboard_creation(self):
        """Test that a leaderboard entry can be created."""
        self.assertEqual(self.leaderboard_entry.user_email, "john@example.com")
        self.assertEqual(self.leaderboard_entry.total_calories, 1500)
        self.assertEqual(self.leaderboard_entry.total_activities, 10)
        self.assertEqual(self.leaderboard_entry.rank, 1)
        self.assertIsNotNone(self.leaderboard_entry.updated_at)

    def test_leaderboard_string_representation(self):
        """Test the string representation of a leaderboard entry."""
        self.assertEqual(str(self.leaderboard_entry), "john@example.com - Rank 1")

    def test_leaderboard_ordering(self):
        """Test that leaderboard entries are ordered by rank."""
        Leaderboard.objects.create(
            user_email="jane@example.com",
            total_calories=1200,
            total_activities=8,
            rank=2
        )
        entries = Leaderboard.objects.all()
        self.assertEqual(entries[0].rank, 1)
        self.assertEqual(entries[1].rank, 2)


class WorkoutModelTest(TestCase):
    """Tests for the Workout model."""

    def setUp(self):
        """Set up test data."""
        self.workout = Workout.objects.create(
            name="Morning Run",
            description="A refreshing morning run to start the day",
            difficulty="Medium",
            duration=30,
            calories_estimate=300
        )

    def test_workout_creation(self):
        """Test that a workout can be created."""
        self.assertEqual(self.workout.name, "Morning Run")
        self.assertEqual(self.workout.description, "A refreshing morning run to start the day")
        self.assertEqual(self.workout.difficulty, "Medium")
        self.assertEqual(self.workout.duration, 30)
        self.assertEqual(self.workout.calories_estimate, 300)
        self.assertIsNotNone(self.workout.created_at)

    def test_workout_string_representation(self):
        """Test the string representation of a workout."""
        self.assertEqual(str(self.workout), "Morning Run")
