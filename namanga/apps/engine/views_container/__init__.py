from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

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

from namanga.apps.engine.models import User
from namanga.apps.engine.utils.constant import AppStatus
# from velociti.apps.engine.utils.helper import is_valid_uuid4, is_valid_email
# from velociti.apps.engine.models_container.enum_type import TypeTransactionEnum
# from velociti.apps.engine.models_container.enum_type import SystemRoleUserUpdateEnum, SystemRoleEnum
# from velociti.apps.engine.serializers import (UserRegisterSerializer, UserSerializer, UserConfirmNewPasswordSerializer,
#                                               UserForgotPasswordSerializer, UserDeleteAccountSerializer,
#                                               CreatePaymentSerializers, HistoryBalance, HistoryBalanceSerializer,
#                                               Notifications, NotificationsSerializer)
# # from velociti.apps.engine.utils.constant import ResponseData, AppStatus
# from velociti.apps.engine.permissions import UserPermissionChecker

