from namanga.apps.engine.serializers import (
    UserRegisterSerializer, UserSerializer
)

from namanga.apps.engine.utils.send_email import sent_mail_verification
from namanga.apps.engine.views_container import (
    User, GenericAPIView, Response, status, swagger_auto_schema, openapi,
    timezone, AppStatus
)


class RegisterViewSet(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            sent_mail_verification(user)
            return Response(AppStatus.SEND_MAIL_SUCCESS.message)
        else:
            user = User.objects.filter(email=serializer.data['email']).first()
            if user and not user.is_active:
                user.set_password(serializer.data['password'])
                user.full_name = serializer.data['username']
                user.save()
                sent_mail_verification(user)
                return Response(AppStatus.SEND_MAIL_SUCCESS.message)
            return Response(serializer.errors)


class ResendVerificationViewSet(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING),
        },
        required=['email']),
    )
    def put(self, request):
        email = request.data['email']
        user = User.objects.filter(email=email).first()
        if user:
            sent_mail_verification(user)
            return Response(AppStatus.SEND_MAIL_SUCCESS.message)
        else:
            return Response(AppStatus.EMAIL_NOT_EXIST.message, status=status.HTTP_404_NOT_FOUND)


class VerifyCodeViewSet(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'verify_code': openapi.Schema(type=openapi.TYPE_STRING)
        },
        required=['email', 'verify_code']),
    )
    def post(self, request):
        email = request.data['email']
        verify_code = request.data['verify_code']
        user = User.objects.filter(email=email).first()
        if user:
            if user.verify_code == verify_code:
                if user.code_lifetime >= timezone.now():
                    user.is_active = True
                    user.save()
                    return Response(AppStatus.REGISTER_USER_SUCCESS.message)
                return Response(AppStatus.EXPIRED_VERIFY_CODE.message)
            else:
                return Response(AppStatus.INVALID_VERIFY_CODE.message)
        else:
            return Response(AppStatus.EMAIL_NOT_EXIST.message)

