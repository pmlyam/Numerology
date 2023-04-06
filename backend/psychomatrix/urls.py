from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import SquareOfPythagorasView

urlpatterns = [
    path('api/', SquareOfPythagorasView.as_view(), name="square"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
