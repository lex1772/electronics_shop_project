from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from suppliers.models import Link


# Create your tests here.
class LinkTestCase(APITestCase):
    # Тесты для привычек
    def setUp(self) -> None:
        # Создание звена сети и пользователя для тестирования
        self.username = 'a'
        self.password = '12345'
        self.user = User.objects.create(
            username=self.username, password=self.password, is_active=True)

        self.link = Link.objects.create(
            name="Завод"
        )

    def test_get_list(self):
        # Получение списка звеньев сети и сравнение с названием первого звена
        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse('suppliers:link_list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['name'], 'Завод')

    def test_link_update(self):
        # Обновление звена сети и сравнение с обновленным емейлом
        self.client.force_authenticate(self.user)
        response = self.client.patch(
            reverse(
                'suppliers:link_update',
                kwargs={'pk': self.link.pk}
            ),
            data={
                'email': 'a@a.ru', 'country': 'a',
                'city': 'a', 'street': 'a', 'house': 'a'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['contacts'][0]['email'], 'a@a.ru')

    def test_link_create(self):
        # Создание звена сети и сравнение с количеством звеньев сети
        self.client.force_authenticate(self.user)
        data = {
            "name": "магазин",
            "supplier": self.link.pk
        }
        response = self.client.post(
            reverse('suppliers:link_create'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Link.objects.all().count(), 2)

    def test_link_detail(self):
        # Просмотр звена сети
        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse('suppliers:link', kwargs={'pk': self.link.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_delete(self):
        # Удаление звена сети
        self.client.force_authenticate(self.user)
        response = (
            self.client.delete(
                reverse(
                    'suppliers:link_delete',
                    kwargs={'pk': self.link.pk})
            )
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
