from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection


# Import models from octofit_tracker.models
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')

        # Create activities
        Activity.objects.create(user='ironman', team='Marvel', activity_type='Running', duration=30)
        Activity.objects.create(user='batman', team='DC', activity_type='Cycling', duration=45)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Create workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for superheroes')
        Workout.objects.create(name='Speed Run', description='Speed workout for superheroes')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
