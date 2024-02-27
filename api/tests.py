from django.test import TestCase
from django.utils import timezone
from unittest.mock import patch
from .models import SubEmail
from .sendmail import send_schedule_email
from django.urls import reverse
from django.core import mail
from rest_framework.test import APIClient
from django.conf import settings


class SendScheduledEmailTestCase(TestCase):
    def test_send_weekly_email(self):
        sub_email = SubEmail.objects.create(
            name='JhonDoe',
            email='test@example.com',
            sub_state=True,
            frequency='weekly',
            last_sent=timezone.now() - timezone.timedelta(weeks=7)
        )
        with patch('api.sendmail.send_mail') as mock_send_mail:
            send_schedule_email()
            # Ensure that send_mail was called
            self.assertTrue(mock_send_mail.called)

            # Check the arguments passed to send_mail
            args, kwargs = mock_send_mail.call_args
            self.assertEqual(
                args[0], f"This is your weekly newsletter")  # subject
            self.assertIn('Hi JhonDoe,', args[1])  # body
            self.assertEqual(
                args[2], settings.EMAIL_HOST_USER)  # from_email
            self.assertEqual(args[3], ['test@example.com'])  # recipient list
            self.assertFalse(kwargs['fail_silently'])  # fail_silently

            # Check if the last_sent attribute was updated
            sub_email.refresh_from_db()
            self.assertGreaterEqual(
                sub_email.last_sent, timezone.now() - timezone.timedelta(days=1))

    def test_send_monthly_email(self):
        sub_email = SubEmail.objects.create(
            name='JhonDoe',
            email='test@mail.com',
            sub_state=True,
            frequency='monthly',
            last_sent=timezone.now() - timezone.timedelta(days=30)
        )
        with patch('api.sendmail.send_mail') as mock_send_mail:
            send_schedule_email()
            # Ensure that send_mail was called
            self.assertTrue(mock_send_mail.called)

            # Check the arguments passed to send_mail
            args, kwargs = mock_send_mail.call_args
            self.assertEqual(
                args[0], f"This is your monthly newsletter")
            self.assertIn('Hi JhonDoe,', args[1])
            self.assertEqual(
                args[2], settings.EMAIL_HOST_USER)
            self.assertEqual(args[3], ['test@mail.com'])
            self.assertFalse(kwargs['fail_silently'])

            # Check if the last_sent attribute was updated
            sub_email.refresh_from_db()
            self.assertGreaterEqual(
                sub_email.last_sent, timezone.now() - timezone.timedelta(days=1))
