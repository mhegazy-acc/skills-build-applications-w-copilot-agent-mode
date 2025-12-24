
from django.core.management.base import BaseCommand
from octofit_tracker import models as app_models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data using pymongo to avoid Djongo ORM issues
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workout.delete_many({})
        db.user.delete_many({})
        db.team.delete_many({})

        # Create teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create users
        users = [
            app_models.User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            app_models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            app_models.User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            app_models.User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        activities = [
            app_models.Activity.objects.create(user=users[0], type='run', duration=30, distance=5),
            app_models.Activity.objects.create(user=users[1], type='cycle', duration=60, distance=20),
            app_models.Activity.objects.create(user=users[2], type='swim', duration=45, distance=2),
            app_models.Activity.objects.create(user=users[3], type='run', duration=25, distance=4),
        ]

        # Create workouts
        workouts = [
            app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes'),
            app_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes'),
        ]

        # Create leaderboard
        app_models.Leaderboard.objects.create(user=users[0], score=100)
        app_models.Leaderboard.objects.create(user=users[1], score=90)
        app_models.Leaderboard.objects.create(user=users[2], score=95)
        app_models.Leaderboard.objects.create(user=users[3], score=85)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
