from datetime import timedelta
from rest_framework import mixins
from namanga.setting.path import cfg
from os.path import join

from namanga.apps.engine.models import User, Manga
from namanga.apps.engine.serializers import (
    MangaSerializers
)
from namanga.apps.engine.views_container import (
    GenericAPIView, Response, status, permissions, action, APIView, IsAuthenticated, swagger_auto_schema, openapi,
    timezone, make_password, check_password, RefreshToken, ListAPIView, LimitOffsetPagination, GenericViewSet,
    AppStatus, check_role_crud_manga, MultiPartParser, FormParser, os
)


class MangaViewSet(GenericViewSet, mixins.CreateModelMixin,
                   mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = Manga.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = LimitOffsetPagination
    serializer_class = MangaSerializers

    def get_queryset(self):
        name = self.request.query_params.get("name", None)
        author = self.request.query_params.get("author", None)
        queryset = Manga.objects.filter().all()
        if name:
            queryset = queryset.filter(name__icontains=name)

        if author:
            queryset = queryset.filter(author__icontains=author)
        queryset = queryset.order_by("-created_at")
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name="name", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter(name="author", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING), ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CreateMangaViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name="name", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter(name="author", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter(name="introduction", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter(name="image_data", in_=openapi.IN_FORM, type=openapi.TYPE_FILE,
                              description="Image data of manga"), ]
    )
    def post(self, request, *args, **kwargs):
        current_user = request.user
        if not check_role_crud_manga(current_user.role):
            return Response(AppStatus.USER_NOT_HAVE_ENOUGH_PERMISSION.message)
        name = request.query_params.get('name')
        author = request.query_params.get('author')
        introduction = request.query_params.get('introduction')
        image_data = request.data.get('image_data')

        path_image = os.path.join(cfg.DIR_IMAGE_MANGA_PTH, 'avatar_manga')
        os.makedirs(path_image, exist_ok=True)

        file_path = os.path.join(path_image, name + ".png")
        with open(file_path, 'wb') as f:
            f.write(image_data.read())

        manga = Manga(name=name, author=author, introduction=introduction, image=file_path)

        return Response("Manga created successfully", status=status.HTTP_200_OK)


class DeleteMangaViewSet(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MangaSerializers

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name='manga_id', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True, )]
    )
    def delete(self, request, *args, **kwargs):
        current_user = request.user
        if not check_role_crud_manga(current_user.role):
            return Response(AppStatus.USER_NOT_HAVE_ENOUGH_PERMISSION.message)
        manga_id = request.query_params.get("manga_id")
        manga = Manga.objects.filter(id=manga_id).first()

        if not manga:
            return Response(AppStatus.ID_INVALID.message)

        manga.delete()
        return Response(Response("Manga created successfully", status=status.HTTP_200_OK))
