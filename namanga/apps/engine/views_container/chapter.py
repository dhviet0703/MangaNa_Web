from rest_framework import mixins

from namanga.apps.engine.models_container.manga import Manga
from namanga.setting.path import cfg
from namanga.apps.engine.utils.save_image import save_data_image_zip

from namanga.apps.engine.models import User, Chapter
from namanga.apps.engine.serializers import (
    ChapterSerializers
)
from namanga.apps.engine.views_container import (
    GenericAPIView, Response, status, permissions, action, APIView, IsAuthenticated, swagger_auto_schema, openapi,
    timezone, make_password, check_password, RefreshToken, ListAPIView, LimitOffsetPagination, GenericViewSet,
    AppStatus, check_role_crud_manga, MultiPartParser, FormParser, os
)


class ChapterViewSet(GenericViewSet, mixins.CreateModelMixin,
                     mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = Chapter.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = LimitOffsetPagination
    serializer_class = ChapterSerializers

    def get_queryset(self):
        name = self.request.query_params.get("name", None)
        author = self.request.query_params.get("author", None)
        queryset = Chapter.objects.filter().all()
        if name:
            queryset = queryset.filter(name__icontains=name)

        if author:
            queryset = queryset.filter(author__icontains=author)
        queryset = queryset.order_by("-created_at")
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name="name", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter(name="author", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter(name="author", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter(name="author", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter(name="manga_id", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CreateChapterViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name="number", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter(name="title", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter(name="manga_id", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter(name="data_chapter", in_=openapi.IN_FORM, type=openapi.TYPE_FILE,
                              description="Zip file to upload"),
        ]
    )
    def post(self, request, *args, **kwargs):
        current_user = request.user
        if not check_role_crud_manga(current_user.role):
            return Response(AppStatus.USER_NOT_HAVE_ENOUGH_PERMISSION.message)
        number = request.query_params.get('number')
        title = request.query_params.get('title')
        manga_id = request.query_params.get('manga_id')
        data_chapter = request.FILES.get('data_chapter')

        manga = Manga.objects.get(id=manga_id)

        path_image = os.path.join(cfg.DIR_IMAGE_MANGA_PTH, 'data_manga')
        path_image = os.path.join(path_image, str(number))
        os.makedirs(path_image, exist_ok=True)

        chapter = Chapter(manga=manga, number=number, title=title)
        chapter.save()
        save_data_image_zip(chapter.id, path_image, data_chapter)
        manga.total_chapter += 1
        manga.save()

        return Response("Chapter created successfully", status=status.HTTP_200_OK)


class UpdateViewsChapterViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name="chapter_id", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def put(self, request, *args, **kwargs):
        current_user = request.user
        chapter_id = request.query_params.get('chapter_id')
        chapter = Chapter.objects.filter(id=chapter_id).first()
        chapter.views += 1

        manga = Manga.objects.filter(id=chapter.manga_id).first()
        manga.views += 1
        chapter.save()
        manga.save()

        return Response("Update views successfully", status=status.HTTP_200_OK)



class DeleteChapterViewSet(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChapterSerializers

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name='chapter_id', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True, )]
    )
    def delete(self, request, *args, **kwargs):
        current_user = request.user
        if not check_role_crud_manga(current_user.role):
            return Response(AppStatus.USER_NOT_HAVE_ENOUGH_PERMISSION.message)
        chapter_id = request.query_params.get("chapter_id")
        chapter = Chapter.objects.filter(id=chapter_id).first()

        if not chapter:
            return Response(AppStatus.ID_INVALID.message)

        chapter.delete()
        return Response(Response("Chapter created successfully", status=status.HTTP_200_OK))
