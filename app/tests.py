from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from .models import Issue, Project
from django.utils import timezone

User = get_user_model()


class BcTestCase(TestCase):
    client = Client()

    def setUp(self):
        user = User.objects.create(username='renataberoli')
        user.set_password('123and4')
        user.save()
        return user

    def test_login_failed(self):
        response = self.client.post('/accounts/login/', {'username': 'beroli', 'password': '1234'})
        self.assertIn(b"correct username", response.content)

    def test_login_success(self):
        response = self.client.post('/accounts/login/', {'username': 'renataberoli', 'password': '123and4'})
        self.assertRedirects(response, '/')

    def test_search_filter(self):
        user = User.objects.get(username="renataberoli")
        date = timezone.now()
        Issue.objects.create(title='Slow internet error', author=user, creation_date=date)
        Issue.objects.create(title='Teste title 2', author=user, creation_date=date)

        self.client.login(username='renataberoli', password='123and4')
        response = self.client.get("/", {"data": "error"})
        self.assertIn(b"Slow internet error", response.content)
        self.assertNotIn(b"Teste title 2", response.content)

    def test_priority_filter(self):
        user = User.objects.get(username="renataberoli")
        date = timezone.now()
        Issue.objects.create(title='Test issue with priority urgent', author=user, creation_date=date, priority='1')
        Issue.objects.create(title='Test issue with priority normal', author=user, creation_date=date, priority='3')

        self.client.login(username='renataberoli', password='123and4')
        response = self.client.get('/', {'priority': '1'})
        self.assertIn(b"Test issue with priority urgent", response.content)
        self.assertNotIn(b"Test issue with priority normal", response.content)

    def test_status_filter(self):
        user = User.objects.get(username="renataberoli")
        date = timezone.now()
        Issue.objects.create(title='Test issue with status closed', author=user, creation_date=date, status='closed')
        Issue.objects.create(title='Test issue with status open', author=user, creation_date=date, status='open')

        self.client.login(username='renataberoli', password='123and4')
        response = self.client.get('/', {'status': 'closed'})
        self.assertIn(b"Test issue with status closed", response.content)
        self.assertNotIn(b"Test issue with status open", response.content)

    def test_all_filters_together(self):
        user = User.objects.get(username="renataberoli")
        Issue.objects.create(title='Test issue with all arguments - error', author=user, priority='1', status='open',
                             label='frontend', assignee=user)
        Issue.objects.create(title='Test issue without data arguments', author=user, priority='1', status='open',
                             label='frontend', assignee=user)

        self.client.login(username='renataberoli', password='123and4')
        response = self.client.get('/', {'data': 'error', 'priority': '1', 'status': 'open', 'label': 'frontend',
                                         'assignee': user.id})

        self.assertIn(b"Test issue with all arguments - error", response.content)
        self.assertNotIn(b"Test issue without data arguments", response.content)

    def test_issue_creation(self):
        user = User.objects.get(username="renataberoli")

        self.client.login(username='renataberoli', password='123and4')
        project = Project.objects.create(name='Acme')
        response = self.client.post('/issue/new/', {'title': 'Test issue if issue is created', 'assignee': user.id,
                                                    'project': project.id, 'status': 'open'})

        issue = Issue.objects.get(title='Test issue if issue is created')
        self.assertRedirects(response, f'/issue/{issue.id}/')

