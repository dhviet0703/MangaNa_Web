from rest_framework import mixins

from namanga.apps.engine.models import History
from namanga.apps.engine.serializers import (
    HistorySerializers, CreateHistorySerializers, UpdateHistorySerializers
)
from namanga.apps.engine.views_container import (
    GenericAPIView, Response, permissions, LimitOffsetPagination, GenericViewSet,
    AppStatus
)


class HistoryViewSet(GenericViewSet, mixins.CreateModelMixin,
                     mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = History.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HistorySerializers
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateHistorySerializers
        elif self.request.method == 'PUT':
            return UpdateHistorySerializers
        return HistorySerializers

    def get_queryset(self):
        queryset = History.objects.all()
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(user=user)
        else:
            return None

        queryset = queryset.filter(user=user)
        queryset = queryset.order_by("-created_at")
        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class HistoryDeleteViewSet(GenericAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializers
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response(AppStatus.USER_NOT_HAVE_ENOUGH_PERMISSION.message)
        instance = self.get_object()
        instance.delete()
        return Response()
