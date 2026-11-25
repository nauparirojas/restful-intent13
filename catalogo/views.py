from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filterset_fields = ['estado', 'categoria', 'codigo']
    search_fields = ['nombre', 'codigo', 'categoria']
    ordering_fields = ['precio', 'stock', 'creado_en', 'nombre']
    ordering = ['-creado_en']

    @action(detail=True, methods=['post'])
    def activar(self, request, pk=None):
        producto = self.get_object()
        if producto.stock <= 0:
            return Response(
                {'detail': 'No se puede activar un producto sin stock disponible.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        producto.estado = 'activo'
        producto.save(update_fields=['estado'])
        serializer = self.get_serializer(producto)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def disponibles(self, request):
        qs = self.filter_queryset(self.get_queryset().filter(estado='activo', stock__gt=0))
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)