from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Limpar dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Criar times
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman'])

        # Criar usuários
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='cap@marvel.com', name='Captain America', team='Marvel'),
            User(email='thor@marvel.com', name='Thor', team='Marvel'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Criar atividades
        Activity.objects.create(user='Iron Man', type='Run', duration=30, date=timezone.now().date())
        Activity.objects.create(user='Superman', type='Swim', duration=45, date=timezone.now().date())

        # Criar leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Criar workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Power Circuit', description='Strength for DC heroes', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
