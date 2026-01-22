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
        
        # Create teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Avengers assemble! Earth\'s Mightiest Heroes working together for fitness.'
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League united! The world\'s greatest superheroes training for excellence.'
        )
        
        marvel_id = str(team_marvel._id)
        dc_id = str(team_dc._id)
        
        self.stdout.write('Creating users...')
        
        # Create Marvel users
        iron_man = User.objects.create(
            name='Tony Stark (Iron Man)',
            email='tony@starkindustries.com',
            password='ironman123',
            team_id=marvel_id
        )
        
        captain_america = User.objects.create(
            name='Steve Rogers (Captain America)',
            email='steve@avengers.com',
            password='shield123',
            team_id=marvel_id
        )
        
        thor = User.objects.create(
            name='Thor Odinson',
            email='thor@asgard.com',
            password='mjolnir123',
            team_id=marvel_id
        )
        
        black_widow = User.objects.create(
            name='Natasha Romanoff (Black Widow)',
            email='natasha@shield.com',
            password='widow123',
            team_id=marvel_id
        )
        
        hulk = User.objects.create(
            name='Bruce Banner (Hulk)',
            email='bruce@gamma.com',
            password='smash123',
            team_id=marvel_id
        )
        
        # Create DC users
        superman = User.objects.create(
            name='Clark Kent (Superman)',
            email='clark@dailyplanet.com',
            password='krypton123',
            team_id=dc_id
        )
        
        batman = User.objects.create(
            name='Bruce Wayne (Batman)',
            email='bruce@wayneenterprises.com',
            password='gotham123',
            team_id=dc_id
        )
        
        wonder_woman = User.objects.create(
            name='Diana Prince (Wonder Woman)',
            email='diana@themyscira.com',
            password='amazon123',
            team_id=dc_id
        )
        
        flash = User.objects.create(
            name='Barry Allen (Flash)',
            email='barry@starlabs.com',
            password='speedforce123',
            team_id=dc_id
        )
        
        aquaman = User.objects.create(
            name='Arthur Curry (Aquaman)',
            email='arthur@atlantis.com',
            password='trident123',
            team_id=dc_id
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
            calories=600,
            date=base_date + timedelta(days=1),
            notes='Testing new arc reactor powered bike'
        )
        Activity.objects.create(
            user_id=str(iron_man._id),
            activity_type='Strength Training',
            duration=45,
            calories=400,
            date=base_date + timedelta(days=3),
            notes='Suit calibration workout'
        )
        
        # Captain America - classic training
        Activity.objects.create(
            user_id=str(captain_america._id),
            activity_type='Running',
            duration=90,
            calories=900,
            date=base_date + timedelta(days=1),
            notes='Morning run around the city'
        )
        Activity.objects.create(
            user_id=str(captain_america._id),
            activity_type='Boxing',
            duration=60,
            calories=700,
            date=base_date + timedelta(days=2),
            notes='Training with the punching bag'
        )
        
        # Thor - god-like workouts
        Activity.objects.create(
            user_id=str(thor._id),
            activity_type='Strength Training',
            duration=120,
            calories=1200,
            date=base_date + timedelta(days=1),
            notes='Mjolnir lifting practice'
        )
        Activity.objects.create(
            user_id=str(thor._id),
            activity_type='Cardio',
            duration=75,
            calories=800,
            date=base_date + timedelta(days=4),
            notes='Asgardian warrior training'
        )
        
        # Black Widow - agility focused
        Activity.objects.create(
            user_id=str(black_widow._id),
            activity_type='Yoga',
            duration=60,
            calories=300,
            date=base_date + timedelta(days=2),
            notes='Flexibility and balance training'
        )
        Activity.objects.create(
            user_id=str(black_widow._id),
            activity_type='Martial Arts',
            duration=90,
            calories=750,
            date=base_date + timedelta(days=5),
            notes='Combat training session'
        )
        
        # Hulk - smashing workouts
        Activity.objects.create(
            user_id=str(hulk._id),
            activity_type='Strength Training',
            duration=100,
            calories=1100,
            date=base_date + timedelta(days=1),
            notes='Controlled strength exercises'
        )
        Activity.objects.create(
            user_id=str(hulk._id),
            activity_type='Cardio',
            duration=45,
            calories=500,
            date=base_date + timedelta(days=6),
            notes='Stress management workout'
        )
        
        # Superman - super-powered training
        Activity.objects.create(
            user_id=str(superman._id),
            activity_type='Flying',
            duration=120,
            calories=1500,
            date=base_date + timedelta(days=1),
            notes='High altitude flight training'
        )
        Activity.objects.create(
            user_id=str(superman._id),
            activity_type='Strength Training',
            duration=90,
            calories=1000,
            date=base_date + timedelta(days=3),
            notes='Fortress of Solitude workout'
        )
        
        # Batman - intense detective training
        Activity.objects.create(
            user_id=str(batman._id),
            activity_type='Martial Arts',
            duration=120,
            calories=1100,
            date=base_date + timedelta(days=1),
            notes='Batcave training session'
        )
        Activity.objects.create(
            user_id=str(batman._id),
            activity_type='Running',
            duration=60,
            calories=650,
            date=base_date + timedelta(days=2),
            notes='Rooftop parkour'
        )
        
        # Wonder Woman - warrior training
        Activity.objects.create(
            user_id=str(wonder_woman._id),
            activity_type='Sword Fighting',
            duration=90,
            calories=900,
            date=base_date + timedelta(days=1),
            notes='Themysciran combat practice'
        )
        Activity.objects.create(
            user_id=str(wonder_woman._id),
            activity_type='Strength Training',
            duration=75,
            calories=800,
            date=base_date + timedelta(days=4),
            notes='Lasso training'
        )
        
        # Flash - speed training
        Activity.objects.create(
            user_id=str(flash._id),
            activity_type='Running',
            duration=30,
            calories=1200,
            date=base_date + timedelta(days=1),
            notes='Speed force sprint around the city'
        )
        Activity.objects.create(
            user_id=str(flash._id),
            activity_type='Cardio',
            duration=45,
            calories=900,
            date=base_date + timedelta(days=3),
            notes='High-speed interval training'
        )
        
        # Aquaman - aquatic workouts
        Activity.objects.create(
            user_id=str(aquaman._id),
            activity_type='Swimming',
            duration=120,
            calories=1300,
            date=base_date + timedelta(days=1),
            notes='Deep ocean exploration swim'
        )
        Activity.objects.create(
            user_id=str(aquaman._id),
            activity_type='Strength Training',
            duration=60,
            calories=700,
            date=base_date + timedelta(days=5),
            notes='Trident training underwater'
        )
        
        self.stdout.write('Calculating leaderboard...')
        
        # Calculate team statistics
        marvel_calories = sum([
            1000, 1100, 2000, 1050, 1600  # Iron Man, Cap, Thor, Widow, Hulk
        ])
        marvel_activities = 10
        
        dc_calories = sum([
            2500, 1750, 1700, 2100, 2000  # Superman, Batman, Wonder Woman, Flash, Aquaman
        ])
        dc_activities = 10
        
        # Create leaderboard entries
        Leaderboard.objects.create(
            team_id=dc_id,
            total_calories=dc_calories,
            total_activities=dc_activities,
            rank=1
        )
        
        Leaderboard.objects.create(
            team_id=marvel_id,
            total_calories=marvel_calories,
            total_activities=marvel_activities,
            rank=2
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
