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
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes'
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League Champions'
        )

        self.stdout.write('Creating users...')
        
        # Create Marvel users
        marvel_users = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com'},
            {'name': 'Steve Rogers', 'email': 'captainamerica@marvel.com'},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com'},
        ]
        
        # Create DC users
        dc_users = [
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com'},
            {'name': 'Clark Kent', 'email': 'superman@dc.com'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com'},
        ]

        created_users = []
        
        for user_data in marvel_users:
            user = User.objects.create(
                name=user_data['name'],
                email=user_data['email'],
                team='Team Marvel'
            )
            created_users.append(user)
        
        for user_data in dc_users:
            user = User.objects.create(
                name=user_data['name'],
                email=user_data['email'],
                team='Team DC'
            )
            created_users.append(user)

        self.stdout.write('Creating workouts...')
        
        # Create workouts
        workouts = [
            {
                'name': 'Super Soldier Training',
                'description': 'High-intensity workout designed by Captain America',
                'difficulty': 'Hard',
                'duration': 60,
                'calories_estimate': 800
            },
            {
                'name': 'Asgardian Warrior Routine',
                'description': 'Thor\'s legendary strength training',
                'difficulty': 'Extreme',
                'duration': 90,
                'calories_estimate': 1200
            },
            {
                'name': 'Spider-Sense Agility',
                'description': 'Web-slinger\'s agility and flexibility workout',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_estimate': 600
            },
            {
                'name': 'Bat-Training',
                'description': 'Batman\'s dark knight conditioning',
                'difficulty': 'Hard',
                'duration': 75,
                'calories_estimate': 950
            },
            {
                'name': 'Kryptonian Power Workout',
                'description': 'Superman\'s strength and endurance training',
                'difficulty': 'Extreme',
                'duration': 120,
                'calories_estimate': 1500
            },
            {
                'name': 'Amazonian Combat Training',
                'description': 'Wonder Woman\'s warrior workout',
                'difficulty': 'Hard',
                'duration': 60,
                'calories_estimate': 850
            },
            {
                'name': 'Speed Force Cardio',
                'description': 'Flash\'s lightning-fast cardio routine',
                'difficulty': 'Medium',
                'duration': 30,
                'calories_estimate': 700
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write('Creating activities...')
        
        # Create activities for each user
        activity_types = [
            'Running', 'Swimming', 'Cycling', 'Weight Training', 
            'Boxing', 'Yoga', 'CrossFit', 'Martial Arts'
        ]
        
        for user in created_users:
            # Create 5-10 random activities per user
            num_activities = random.randint(5, 10)
            for i in range(num_activities):
                days_ago = random.randint(0, 30)
                activity_date = datetime.now() - timedelta(days=days_ago)
                duration = random.randint(20, 120)
                calories = duration * random.randint(8, 15)
                
                Activity.objects.create(
                    user_email=user.email,
                    activity_type=random.choice(activity_types),
                    duration=duration,
                    calories_burned=calories,
                    date=activity_date
                )

        self.stdout.write('Creating leaderboard...')
        
        # Calculate leaderboard data
        leaderboard_data = []
        for user in created_users:
            activities = Activity.objects.filter(user_email=user.email)
            total_calories = sum(activity.calories_burned for activity in activities)
            total_activities = activities.count()
            
            leaderboard_data.append({
                'user_email': user.email,
                'total_calories': total_calories,
                'total_activities': total_activities
            })
        
        # Sort by total calories and assign ranks
        leaderboard_data.sort(key=lambda x: x['total_calories'], reverse=True)
        
        for rank, data in enumerate(leaderboard_data, start=1):
            Leaderboard.objects.create(
                user_email=data['user_email'],
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
