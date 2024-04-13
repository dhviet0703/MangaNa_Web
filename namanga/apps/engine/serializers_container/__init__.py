import random
from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction
from django.utils import timezone
from django.utils.html import strip_tags
from rest_framework import serializers
from rest_framework.response import Response

# from velociti.apps.engine.utils.template_mail import *
# from velociti.apps.engine.utils.template_mail import TemplateMail
from namanga.apps.engine.utils.constant import AppStatus
