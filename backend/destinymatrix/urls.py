from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import MatrixOfDestinyView

urlpatterns = [
    path('destinymatrix/', MatrixOfDestinyView.as_view(), name="destiny"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
