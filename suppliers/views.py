from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from suppliers.models import Link
from suppliers.serializers import LinkSerializer, LinkCreateOrUpdateSerializer


class LinkCreateAPIView(generics.CreateAPIView):
    # Контроллер для создания объектов сети
    serializer_class = LinkCreateOrUpdateSerializer
    permission_classes = [IsAuthenticated]


class LinkListAPIView(generics.ListAPIView):
    # Контроллер для получения списков объектов сети
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('contact__country',)
    permission_classes = [IsAuthenticated]


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    # Контроллер для получения объекта сети
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]


class LinkUpdateAPIView(generics.UpdateAPIView):
    # Контроллер для обновления объекта сети
    serializer_class = LinkCreateOrUpdateSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]


class LinkDestroyAPIView(generics.DestroyAPIView):
    # Контроллер для удаления объекта сети
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]
