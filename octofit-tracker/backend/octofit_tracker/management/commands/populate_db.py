from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from bson import ObjectId
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write('Creating teams...')
        
        # Create teams with different creation dates
        base_team_date = datetime.now() - timedelta(days=60)
        
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Avengers assemble! Earth\'s Mightiest Heroes working together for fitness.',
            created_at=base_team_date
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League united! The world\'s greatest superheroes training for excellence.',
            created_at=base_team_date + timedelta(days=1)
        )
        
        marvel_id = str(team_marvel._id)
        dc_id = str(team_dc._id)
        
        self.stdout.write('Creating users...')
        
        # Base date for user creation - users join over time
        base_user_date = datetime.now() - timedelta(days=45)
        
        # Create Marvel users
        iron_man = User.objects.create(
            name='Tony Stark (Iron Man)',
            email='tony@starkindustries.com',
            password='ironman123',
            team_id=marvel_id,
            created_at=base_user_date
        )
        
        captain_america = User.objects.create(
            name='Steve Rogers (Captain America)',
            email='steve@avengers.com',
            password='shield123',
            team_id=marvel_id,
            created_at=base_user_date + timedelta(days=2)
        )
        
        thor = User.objects.create(
            name='Thor Odinson',
            email='thor@asgard.com',
            password='mjolnir123',
            team_id=marvel_id,
            created_at=base_user_date + timedelta(days=5)
        )
        
        black_widow = User.objects.create(
            name='Natasha Romanoff (Black Widow)',
            email='natasha@shield.com',
            password='widow123',
            team_id=marvel_id,
            created_at=base_user_date + timedelta(days=8)
        )
        
        hulk = User.objects.create(
            name='Bruce Banner (Hulk)',
            email='bruce@gamma.com',
            password='smash123',
            team_id=marvel_id,
            created_at=base_user_date + timedelta(days=12)
        )
        
        # Create DC users
        superman = User.objects.create(
            name='Clark Kent (Superman)',
            email='clark@dailyplanet.com',
            password='krypton123',
            team_id=dc_id,
            created_at=base_user_date + timedelta(days=3)
        )
        
        batman = User.objects.create(
            name='Bruce Wayne (Batman)',
            email='bruce@wayneenterprises.com',
            password='gotham123',
            team_id=dc_id,
            created_at=base_user_date + timedelta(days=6)
        )
        
        wonder_woman = User.objects.create(
            name='Diana Prince (Wonder Woman)',
            email='diana@themyscira.com',
            password='amazon123',
            team_id=dc_id,
            created_at=base_user_date + timedelta(days=10)
        )
        
        flash = User.objects.create(
            name='Barry Allen (Flash)',
            email='barry@starlabs.com',
            password='speedforce123',
            team_id=dc_id,
            created_at=base_user_date + timedelta(days=14)
        )
        
        aquaman = User.objects.create(
            name='Arthur Curry (Aquaman)',
            email='arthur@atlantis.com',
            password='trident123',
            team_id=dc_id,
            created_at=base_user_date + timedelta(days=18)
        )
        
        marvel_users = [iron_man, captain_america, thor, black_widow, hulk]
        dc_users = [superman, batman, wonder_woman, flash, aquaman]
        
        self.stdout.write('Creating activities...')
        
        # Create activities for Marvel users
        base_date = datetime.now() - timedelta(days=30)
        
        # Iron Man - loves technology-assisted workouts
        Activity.objects.create(
            user_id=str(iron_man._id),
            activity_type='Cycling',
            duration=60,
            distance=25.5,
            calories=600,
            date=base_date + timedelta(days=1),
            notes='Testing new arc reactor powered bike'
        )
        Activity.objects.create(
            user_id=str(iron_man._id),
            activity_type='Strength Training',
            duration=45,
            distance=None,
            calories=400,
            date=base_date + timedelta(days=3),
            notes='Suit calibration workout'
        )
        
        # Captain America - classic training
        Activity.objects.create(
            user_id=str(captain_america._id),
            activity_type='Running',
            duration=90,
            distance=15.0,
            calories=900,
            date=base_date + timedelta(days=1),
            notes='Morning run around the city'
        )
        Activity.objects.create(
            user_id=str(captain_america._id),
            activity_type='Boxing',
            duration=60,
            distance=None,
            calories=700,
            date=base_date + timedelta(days=2),
            notes='Training with the punching bag'
        )
        
        # Thor - god-like workouts
        Activity.objects.create(
            user_id=str(thor._id),
            activity_type='Strength Training',
            duration=120,
            distance=None,
            calories=1200,
            date=base_date + timedelta(days=1),
            notes='Mjolnir lifting practice'
        )
        Activity.objects.create(
            user_id=str(thor._id),
            activity_type='Cardio',
            duration=75,
            distance=None,
            calories=800,
            date=base_date + timedelta(days=4),
            notes='Asgardian warrior training'
        )
        
        # Black Widow - agility focused
        Activity.objects.create(
            user_id=str(black_widow._id),
            activity_type='Yoga',
            duration=60,
            distance=None,
            calories=300,
            date=base_date + timedelta(days=2),
            notes='Flexibility and balance training'
        )
        Activity.objects.create(
            user_id=str(black_widow._id),
            activity_type='Martial Arts',
            duration=90,
            distance=None,
            calories=750,
            date=base_date + timedelta(days=5),
            notes='Combat training session'
        )
        
        # Hulk - smashing workouts
        Activity.objects.create(
            user_id=str(hulk._id),
            activity_type='Strength Training',
            duration=100,
            distance=None,
            calories=1100,
            date=base_date + timedelta(days=1),
            notes='Controlled strength exercises'
        )
        Activity.objects.create(
            user_id=str(hulk._id),
            activity_type='Cardio',
            duration=45,
            distance=None,
            calories=500,
            date=base_date + timedelta(days=6),
            notes='Stress management workout'
        )
        
        # Superman - super-powered training
        Activity.objects.create(
            user_id=str(superman._id),
            activity_type='Flying',
            duration=120,
            distance=500.0,
            calories=1500,
            date=base_date + timedelta(days=1),
            notes='High altitude flight training'
        )
        Activity.objects.create(
            user_id=str(superman._id),
            activity_type='Strength Training',
            duration=90,
            distance=None,
            calories=1000,
            date=base_date + timedelta(days=3),
            notes='Fortress of Solitude workout'
        )
        
        # Batman - intense detective training
        Activity.objects.create(
            user_id=str(batman._id),
            activity_type='Martial Arts',
            duration=120,
            distance=None,
            calories=1100,
            date=base_date + timedelta(days=1),
            notes='Batcave training session'
        )
        Activity.objects.create(
            user_id=str(batman._id),
            activity_type='Running',
            duration=60,
            distance=10.5,
            calories=650,
            date=base_date + timedelta(days=2),
            notes='Rooftop parkour'
        )
        
        # Wonder Woman - warrior training
        Activity.objects.create(
            user_id=str(wonder_woman._id),
            activity_type='Sword Fighting',
            duration=90,
            distance=None,
            calories=900,
            date=base_date + timedelta(days=1),
            notes='Themysciran combat practice'
        )
        Activity.objects.create(
            user_id=str(wonder_woman._id),
            activity_type='Strength Training',
            duration=75,
            distance=None,
            calories=800,
            date=base_date + timedelta(days=4),
            notes='Lasso training'
        )
        
        # Flash - speed training
        Activity.objects.create(
            user_id=str(flash._id),
            activity_type='Running',
            duration=30,
            distance=200.0,
            calories=1200,
            date=base_date + timedelta(days=1),
            notes='Speed force sprint around the city'
        )
        Activity.objects.create(
            user_id=str(flash._id),
            activity_type='Cardio',
            duration=45,
            distance=None,
            calories=900,
            date=base_date + timedelta(days=3),
            notes='High-speed interval training'
        )
        
        # Aquaman - aquatic workouts
        Activity.objects.create(
            user_id=str(aquaman._id),
            activity_type='Swimming',
            duration=120,
            distance=50.0,
            calories=1300,
            date=base_date + timedelta(days=1),
            notes='Deep ocean exploration swim'
        )
        Activity.objects.create(
            user_id=str(aquaman._id),
            activity_type='Strength Training',
            duration=60,
            distance=None,
            calories=700,
            date=base_date + timedelta(days=5),
            notes='Trident training underwater'
        )
        
        self.stdout.write('Calculating leaderboard...')
        
        # Calculate user statistics based on actual activities
        user_stats = {}
        
        # Count activities and calories for each user
        for user in [iron_man, captain_america, thor, black_widow, hulk, superman, batman, wonder_woman, flash, aquaman]:
            activities = Activity.objects.filter(user_id=str(user._id))
            total_calories = sum([a.calories for a in activities])
            total_activities = activities.count()
            user_stats[user] = {
                'calories': total_calories,
                'activities': total_activities
            }
        
        # Sort users by total calories (descending)
        sorted_users = sorted(user_stats.items(), key=lambda x: x[1]['calories'], reverse=True)
        
        # Create leaderboard entries with proper ranks
        for rank, (user, stats) in enumerate(sorted_users, start=1):
            Leaderboard.objects.create(
                user_id=str(user._id),
                total_calories=stats['calories'],
                total_activities=stats['activities'],
                rank=rank
            )
        
        self.stdout.write('Creating workout suggestions...')
        
        # Create workout suggestions
        workouts = [
            Workout.objects.create(
                name='Arc Reactor Cardio Blast',
                description='High-intensity cardio workout powered by cutting-edge technology. Perfect for tech enthusiasts.',
                difficulty='Advanced',
                duration=45,
                calories_estimate=500,
                exercise_type='Cardio'
            ),
            Workout.objects.create(
                name='Super Soldier Strength Training',
                description='Build strength like Captain America with this classic military-style workout.',
                difficulty='Intermediate',
                duration=60,
                calories_estimate=600,
                exercise_type='Strength'
            ),
            Workout.objects.create(
                name='Asgardian Thunder Circuit',
                description='Godly strength training inspired by the mighty Thor. Brings the thunder to your muscles.',
                difficulty='Advanced',
                duration=90,
                calories_estimate=900,
                exercise_type='Strength'
            ),
            Workout.objects.create(
                name='Widow\'s Flexibility Flow',
                description='Enhance flexibility and agility with this Black Widow inspired yoga routine.',
                difficulty='Beginner',
                duration=50,
                calories_estimate=250,
                exercise_type='Yoga'
            ),
            Workout.objects.create(
                name='Hulk Smash HIIT',
                description='High-intensity interval training that\'ll make you feel incredible. Smash those fitness goals!',
                difficulty='Advanced',
                duration=30,
                calories_estimate=400,
                exercise_type='HIIT'
            ),
            Workout.objects.create(
                name='Kryptonian Power Workout',
                description='Superman-level strength training. Reach for the stars with this powerful routine.',
                difficulty='Advanced',
                duration=75,
                calories_estimate=850,
                exercise_type='Strength'
            ),
            Workout.objects.create(
                name='Dark Knight Combat Training',
                description='Master martial arts and combat skills with Batman\'s signature training routine.',
                difficulty='Advanced',
                duration=90,
                calories_estimate=950,
                exercise_type='Martial Arts'
            ),
            Workout.objects.create(
                name='Amazonian Warrior Workout',
                description='Train like Wonder Woman with this warrior-inspired full-body workout.',
                difficulty='Intermediate',
                duration=60,
                calories_estimate=650,
                exercise_type='Full Body'
            ),
            Workout.objects.create(
                name='Speed Force Sprint Session',
                description='Lightning-fast cardio workout inspired by The Flash. Feel the speed force!',
                difficulty='Intermediate',
                duration=40,
                calories_estimate=700,
                exercise_type='Cardio'
            ),
            Workout.objects.create(
                name='Atlantean Aquatic Training',
                description='Dive into fitness with Aquaman\'s underwater-inspired swimming workout.',
                difficulty='Intermediate',
                duration=60,
                calories_estimate=600,
                exercise_type='Swimming'
            ),
        ]
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with superhero test data!'))
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'Created {Workout.objects.count()} workout suggestions')
