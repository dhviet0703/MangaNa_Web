import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models

from namanga.apps.engine.models_container.enum_type import SystemRoleEnum, RoleMangaEnum
