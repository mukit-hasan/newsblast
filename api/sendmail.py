from django.template.loader import render_to_string
from .models import SubEmail
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


def send_schedule_email():
    current_date = timezone.now()
    logger.info('')
    logger.info('Current time: ' + str(current_date))

    try:
        weekly_mails = SubEmail.objects.filter(
            frequency='weekly',
            sub_state=True,
            last_sent__lte=current_date - timezone.timedelta(weeks=1)
        )
        monthly_mails = SubEmail.objects.filter(
            frequency='monthly',
            sub_state=True,
            last_sent__lte=current_date - timezone.timedelta(days=30)
        )
        maillist = weekly_mails | monthly_mails

        logger.info(f"Mail list count: {maillist.count()}")

        for mail in maillist:
            template = render_to_string(
                'api/email.html', {'username': mail.name, 'myname': settings.EMAIL_NAME, 'id': mail.id})
            send_mail(
                f"This is your {mail.frequency} newsletter",
                template,
                settings.EMAIL_HOST_USER,
                [mail.email],
                fail_silently=False,
            )
            mail.last_sent = current_date
            mail.save()

        logger.info("Scheduled emails sent successfully.")

    except Exception as e:
        logger.error(f"An error occurred while sending scheduled emails: {e}")
