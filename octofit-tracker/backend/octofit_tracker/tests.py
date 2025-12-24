from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, User, Activity, Workout, Leaderboard

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Test Team'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserTests(APITestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Test Team')
        url = reverse('user-list')
        data = {'name': 'Test User', 'email': 'test@example.com', 'team': str(team.id)}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        url = reverse('activity-list')
        data = {'user': str(user.id), 'type': 'run', 'duration': 30, 'distance': 5.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {'name': 'Morning Run', 'description': 'A quick morning run.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        url = reverse('leaderboard-list')
        data = {'user': str(user.id), 'score': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
