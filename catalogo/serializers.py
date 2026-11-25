from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Producto


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='producto-detail')
    disponible = serializers.SerializerMethodField()
    creado_en = serializers.ReadOnlyField()
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = [
            'url',
            'id',
            'nombre',
            'codigo',
            'categoria',
            'precio',
            'stock',
            'estado',
            'disponible',
            'creado_en',
            '_links',
        ]
        read_only_fields = ['id', 'creado_en']

    def get_disponible(self, obj):
        return obj.estado == 'activo' and obj.stock > 0

    def get__links(self, obj):
        request = self.context.get('request')
        return {
            'self': reverse('producto-detail', kwargs={'pk': obj.pk}, request=request),
            'collection': reverse('producto-list', request=request),
            'activar': reverse('producto-activar', kwargs={'pk': obj.pk}, request=request),
        }

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError('El precio debe ser mayor a 0.')
        return value

    def validate_codigo(self, value):
        return value.strip().upper()

    def validate(self, attrs):
        estado = attrs.get('estado', getattr(self.instance, 'estado', 'activo'))
        stock = attrs.get('stock', getattr(self.instance, 'stock', 0))
        if estado == 'activo' and stock == 0:
            raise serializers.ValidationError(
                {'stock': 'Un producto en estado activo debe contar con stock mayor a 0.'}
            )
        return attrs