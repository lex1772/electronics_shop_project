from rest_framework import serializers

from suppliers.models import Link


class LinkSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра списка или одного звена сети"""

    contacts = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    debt = serializers.DecimalField(
        max_digits=21, decimal_places=2,
        read_only=True
    )

    extra_kwargs = {
        'email': {'write_only': True},
        'country': {'write_only': True}
    }

    class Meta:
        model = Link
        fields = '__all__'

    def get_contacts(self, instance):
        if instance.contact_set.all():
            return instance.contact_set.all().values()
        return None

    def get_products(self, instance):
        if instance.product_set.all():
            return instance.product_set.all().values()
        return None


class LinkCreateOrUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания или изменения звена сети"""

    contacts = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    email = serializers.EmailField(
        source='contacts.email', default=None
    )
    country = serializers.CharField(
        source='contacts.country', default=None
    )
    city = serializers.CharField(
        source='contacts.city', default=None
    )
    street = serializers.CharField(
        source='contacts.street', default=None
    )
    house = serializers.CharField(
        source='contacts.house', default=None
    )
    debt = serializers.DecimalField(
        max_digits=21, decimal_places=2, read_only=True
    )
    product_name = serializers.CharField(
        source='products.name', default=None
    )
    model = serializers.CharField(
        source='products.model', default=None
    )
    release_date = serializers.DateField(
        source='products.release_date', default=None
    )

    extra_kwargs = {
        'email': {'write_only': True},
        'country': {'write_only': True}
    }

    class Meta:
        model = Link
        fields = '__all__'

    def get_contacts(self, instance):
        if instance.contact_set.all():
            return instance.contact_set.all().values()
        return None

    def get_products(self, instance):
        if instance.product_set.all():
            return instance.product_set.all().values()
        return None
