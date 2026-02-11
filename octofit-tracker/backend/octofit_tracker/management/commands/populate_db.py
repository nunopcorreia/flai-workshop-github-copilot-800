from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating teams...')
        
        # Create teams
        teams_data = [
            {
                'name': 'Team Marvel',
                'description': 'Earth\'s Mightiest Heroes - Assembling fitness champions!'
            },
            {
                'name': 'Team DC',
                'description': 'Justice League Champions - Fighting for fitness and strength!'
            },
            {
                'name': 'Team GitHub',
                'description': 'Open Source Athletes - Collaborating for peak performance!'
            },
            {
                'name': 'Team Octocats',
                'description': 'The Elite Squad - Building better bodies, one commit at a time!'
            },
        ]
        
        created_teams = []
        for team_data in teams_data:
            team = Team.objects.create(**team_data)
            created_teams.append(team)

        self.stdout.write('Creating users...')
        
        # Create users with more realistic data
        users_data = [
            # Team Marvel
            {'username': 'ironman', 'first_name': 'Tony', 'last_name': 'Stark', 'email': 'ironman@marvel.com', 'team': 'Team Marvel'},
            {'username': 'captainamerica', 'first_name': 'Steve', 'last_name': 'Rogers', 'email': 'captainamerica@marvel.com', 'team': 'Team Marvel'},
            {'username': 'thor', 'first_name': 'Thor', 'last_name': 'Odinson', 'email': 'thor@marvel.com', 'team': 'Team Marvel'},
            {'username': 'hulk', 'first_name': 'Bruce', 'last_name': 'Banner', 'email': 'hulk@marvel.com', 'team': 'Team Marvel'},
            {'username': 'blackwidow', 'first_name': 'Natasha', 'last_name': 'Romanoff', 'email': 'blackwidow@marvel.com', 'team': 'Team Marvel'},
            {'username': 'spiderman', 'first_name': 'Peter', 'last_name': 'Parker', 'email': 'spiderman@marvel.com', 'team': 'Team Marvel'},
            
            # Team DC
            {'username': 'batman', 'first_name': 'Bruce', 'last_name': 'Wayne', 'email': 'batman@dc.com', 'team': 'Team DC'},
            {'username': 'superman', 'first_name': 'Clark', 'last_name': 'Kent', 'email': 'superman@dc.com', 'team': 'Team DC'},
            {'username': 'wonderwoman', 'first_name': 'Diana', 'last_name': 'Prince', 'email': 'wonderwoman@dc.com', 'team': 'Team DC'},
            {'username': 'flash', 'first_name': 'Barry', 'last_name': 'Allen', 'email': 'flash@dc.com', 'team': 'Team DC'},
            {'username': 'aquaman', 'first_name': 'Arthur', 'last_name': 'Curry', 'email': 'aquaman@dc.com', 'team': 'Team DC'},
            {'username': 'greenlantern', 'first_name': 'Hal', 'last_name': 'Jordan', 'email': 'greenlantern@dc.com', 'team': 'Team DC'},
            
            # Team GitHub
            {'username': 'octocat', 'first_name': 'Octo', 'last_name': 'Cat', 'email': 'octocat@github.com', 'team': 'Team GitHub'},
            {'username': 'mona', 'first_name': 'Mona', 'last_name': 'Lisa', 'email': 'mona@github.com', 'team': 'Team GitHub'},
            {'username': 'hubber', 'first_name': 'Happy', 'last_name': 'Hubber', 'email': 'hubber@github.com', 'team': 'Team GitHub'},
            {'username': 'coder', 'first_name': 'Elite', 'last_name': 'Coder', 'email': 'coder@github.com', 'team': 'Team GitHub'},
            
            # Team Octocats
            {'username': 'daftpunktocat', 'first_name': 'Daft', 'last_name': 'Punk', 'email': 'daftpunk@octocats.com', 'team': 'Team Octocats'},
            {'username': 'yogitocat', 'first_name': 'Yogi', 'last_name': 'Tocat', 'email': 'yogi@octocats.com', 'team': 'Team Octocats'},
            {'username': 'scubatocat', 'first_name': 'Scuba', 'last_name': 'Tocat', 'email': 'scuba@octocats.com', 'team': 'Team Octocats'},
            {'username': 'surftocat', 'first_name': 'Surf', 'last_name': 'Tocat', 'email': 'surf@octocats.com', 'team': 'Team Octocats'},
        ]

        created_users = []
        for user_data in users_data:
            user = User.objects.create(
                username=user_data['username'],
                name=f"{user_data['first_name']} {user_data['last_name']}",
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email'],
                team=user_data['team']
            )
            created_users.append(user)

        self.stdout.write('Creating workouts...')
        
        # Create diverse workouts with proper difficulty levels
        workouts_data = [
            {
                'name': 'Morning Energizer',
                'description': 'Start your day with a gentle stretch and light cardio routine',
                'difficulty': 'beginner',
                'duration': 20,
                'calories_estimate': 150
            },
            {
                'name': 'Super Soldier Training',
                'description': 'High-intensity workout designed by Captain America for peak performance',
                'difficulty': 'advanced',
                'duration': 60,
                'calories_estimate': 800
            },
            {
                'name': 'Asgardian Warrior Routine',
                'description': 'Thor\'s legendary strength and endurance training from the halls of Asgard',
                'difficulty': 'advanced',
                'duration': 90,
                'calories_estimate': 1200
            },
            {
                'name': 'Spider-Sense Agility',
                'description': 'Web-slinger\'s agility, flexibility, and reflexes workout',
                'difficulty': 'intermediate',
                'duration': 45,
                'calories_estimate': 600
            },
            {
                'name': 'Bat-Training',
                'description': 'Batman\'s dark knight conditioning for stealth and strength',
                'difficulty': 'advanced',
                'duration': 75,
                'calories_estimate': 950
            },
            {
                'name': 'Kryptonian Power Workout',
                'description': 'Superman\'s ultimate strength and endurance training regimen',
                'difficulty': 'advanced',
                'duration': 120,
                'calories_estimate': 1500
            },
            {
                'name': 'Amazonian Combat Training',
                'description': 'Wonder Woman\'s warrior workout combining strength and grace',
                'difficulty': 'advanced',
                'duration': 60,
                'calories_estimate': 850
            },
            {
                'name': 'Speed Force Cardio',
                'description': 'Flash\'s lightning-fast cardio routine for explosive speed',
                'difficulty': 'intermediate',
                'duration': 30,
                'calories_estimate': 700
            },
            {
                'name': 'Yoga Flow for Beginners',
                'description': 'Gentle yoga poses to improve flexibility and mindfulness',
                'difficulty': 'beginner',
                'duration': 30,
                'calories_estimate': 200
            },
            {
                'name': 'HIIT Blast',
                'description': 'High-Intensity Interval Training for maximum calorie burn',
                'difficulty': 'intermediate',
                'duration': 25,
                'calories_estimate': 400
            },
            {
                'name': 'Core Crusher',
                'description': 'Intense abdominal and core strengthening exercises',
                'difficulty': 'intermediate',
                'duration': 20,
                'calories_estimate': 250
            },
            {
                'name': 'Marathon Training',
                'description': 'Long-distance running program for endurance athletes',
                'difficulty': 'advanced',
                'duration': 90,
                'calories_estimate': 1100
            },
        ]
        
        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)

        self.stdout.write('Creating activities...')
        
        # Create diverse activities with distances
        activity_types_with_distance = {
            'running': {'speed_range': (5, 15), 'cal_per_min': (10, 15)},  # km/h
            'cycling': {'speed_range': (15, 30), 'cal_per_min': (8, 12)},
            'swimming': {'speed_range': (2, 4), 'cal_per_min': (11, 14)},
            'walking': {'speed_range': (3, 6), 'cal_per_min': (4, 6)},
        }
        
        activity_types_no_distance = {
            'yoga': {'cal_per_min': (3, 5)},
            'strength': {'cal_per_min': (6, 9)},
            'crossfit': {'cal_per_min': (12, 16)},
            'boxing': {'cal_per_min': (10, 14)},
            'martial arts': {'cal_per_min': (8, 12)},
            'pilates': {'cal_per_min': (4, 6)},
            'hiit': {'cal_per_min': (14, 18)},
        }
        
        all_activity_types = list(activity_types_with_distance.keys()) + list(activity_types_no_distance.keys())
        
        for user in created_users:
            # Create 8-15 random activities per user over the last 30 days
            num_activities = random.randint(8, 15)
            for i in range(num_activities):
                days_ago = random.randint(0, 30)
                activity_date = datetime.now() - timedelta(days=days_ago)
                activity_type = random.choice(all_activity_types)
                duration = random.randint(15, 120)
                
                # Calculate distance and calories based on activity type
                if activity_type in activity_types_with_distance:
                    config = activity_types_with_distance[activity_type]
                    speed_kmh = random.uniform(*config['speed_range'])
                    distance = round((speed_kmh * duration / 60), 2)
                    cal_per_min = random.randint(*config['cal_per_min'])
                else:
                    config = activity_types_no_distance[activity_type]
                    distance = 0.0
                    cal_per_min = random.randint(*config['cal_per_min'])
                
                calories = duration * cal_per_min
                
                Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories_burned=calories,
                    date=activity_date
                )

        self.stdout.write('Creating leaderboard...')
        
        # Calculate leaderboard data with points
        leaderboard_data = []
        for user in created_users:
            activities = Activity.objects.filter(user_email=user.email)
            total_calories = sum(activity.calories_burned for activity in activities)
            total_activities = activities.count()
            total_distance = sum(activity.distance for activity in activities)
            
            # Calculate points: 1 point per calorie, 10 points per activity, 50 points per km
            total_points = total_calories + (total_activities * 10) + int(total_distance * 50)
            
            leaderboard_data.append({
                'user_email': user.email,
                'total_points': total_points,
                'total_calories': total_calories,
                'total_activities': total_activities
            })
        
        # Sort by total points and assign ranks
        leaderboard_data.sort(key=lambda x: x['total_points'], reverse=True)
        
        for rank, data in enumerate(leaderboard_data, start=1):
            Leaderboard.objects.create(
                user_email=data['user_email'],
                total_points=data['total_points'],
                total_calories=data['total_calories'],
                total_activities=data['total_activities'],
                rank=rank
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Workout.objects.count()} workouts')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')

