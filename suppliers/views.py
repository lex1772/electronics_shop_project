from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from contacts.models import Contact
from suppliers.models import Link
from suppliers.serializers import LinkSerializer, LinkCreateOrUpdateSerializer


class LinkCreateAPIView(generics.CreateAPIView):
    # Контроллер для создания объектов сети
    serializer_class = LinkCreateOrUpdateSerializer
    # permission_classes = [IsAuthenticated]


class LinkListAPIView(generics.ListAPIView):
    # Контроллер для получения списков объектов сети
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    # permission_classes = [IsPublic | IsAuthenticated]


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    # Контроллер для получения объекта сети
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    # permission_classes = [IsPublic | IsAuthenticated]


class LinkUpdateAPIView(generics.UpdateAPIView):
    # Контроллер для обновления объекта сети
    serializer_class = LinkCreateOrUpdateSerializer
    queryset = Link.objects.all()
    # permission_classes = [IsOwner]


class LinkDestroyAPIView(generics.DestroyAPIView):
    # Контроллер для удаления объекта сети
    queryset = Link.objects.all()
    # permission_classes = [IsOwner]
