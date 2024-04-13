import random
from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.html import strip_tags

from namanga.apps.engine.utils.template_mail import TemplateMail


def sent_mail_verification(user):
    random_number = random.randint(0, 9999)

    verify_code = "{:04d}".format(random_number)
    user.verify_code = verify_code
    user.code_lifetime = timezone.now() + timedelta(minutes=10)
    user.save()
    message = TemplateMail.CONTENT_MAIL_VERIFICATION(user.username, verify_code)
    send_mail(
        TemplateMail.SUBJECT_MAIL_VERIFICATION,
        strip_tags(message),
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
        html_message=message
    )
