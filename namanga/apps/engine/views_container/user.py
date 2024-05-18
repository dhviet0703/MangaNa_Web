from datetime import timedelta

from namanga.apps.engine.models import User
from namanga.apps.engine.utils.send_email import sent_mail_verification

from namanga.apps.engine.serializers import (
    UserSerializer, UpdateUserSerializer
)
from namanga.apps.engine.views_container import (
    GenericAPIView, Response, status, permissions, action, APIView, IsAuthenticated, swagger_auto_schema, openapi,
    timezone, make_password, check_password, RefreshToken, ListAPIView, LimitOffsetPagination, AppStatus
)


class UserDetailViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    @action(methods=['get'], url_path='/read_me', detail=False)
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[
            openapi.Parameter(
                'username', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True,
            ),]
    )
    @action(methods=['put'], url_path='/update_me', detail=False)
    def put(self, request, *args, **kwargs):
        serializer = UpdateUserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_me = UserSerializer(request.user)
            return Response(user_me.data)
        return Response(serializer.errors)

    
