from django.urls import path
from .views import TarjetaView, PagoView, ComercioView

urlpatterns = [
    path('tarjeta/', TarjetaView.as_view(), name='tarjeta'),
    path('pago/', PagoView.as_view(), name='pago'),
    path('pago/<int:pk>/', PagoView.as_view(), name='pago'), # Para el borrado con ID
    path('comercio/<str:comercio_id>/', ComercioView.as_view(), name='comercio'),
]
