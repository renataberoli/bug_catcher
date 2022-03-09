from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from .models import Issue
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
        logged_in = self.client.login(username='renataberoli', password='123and4')

        user = User.objects.get(username="renataberoli")
        date = timezone.now()
        Issue.objects.create(title='Slow internet in floripa', author=user, creation_date=date)
        Issue.objects.create(title='Teste title 2', author=user, creation_date=date)

        all_issues = Issue.objects.all()
        print(f"All issues: {all_issues}")

        for issue in all_issues:

            self.assertIn('floripa', issue.title)



    def test_priority_filter(self):
        pass

    def test_status_filter(self):
        pass

    def test_label_filter(self):
        pass

    def test_assigned_filter(self):
        pass

    def test_all_filters_together(self):
        pass

