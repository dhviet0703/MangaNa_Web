import os
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.parsers import MultiPartParser, FormParser

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.pagination import LimitOffsetPagination

from namanga.apps.engine.models import User, Manga
from namanga.apps.engine.utils.constant import AppStatus
from namanga.apps.engine.utils.helper import check_role_crud_manga

