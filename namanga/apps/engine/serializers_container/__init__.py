import random
from datetime import timedelta

from os.path import join
from django.conf import settings
from django.db import transaction
from django.utils import timezone
from django.core.mail import send_mail
from rest_framework import serializers
from django.utils.html import strip_tags
from rest_framework.response import Response

from namanga.setting.path import cfg
from namanga.apps.engine.models import *
from namanga.apps.engine.utils.helper import *
from namanga.apps.engine.utils.constant import AppStatus
from namanga.apps.engine.models_container.enum_type import ManGaGenreEnum, SystemRoleEnum
