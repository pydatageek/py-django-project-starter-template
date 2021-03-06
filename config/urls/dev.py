from django.conf import settings
from django.conf.urls.static import static

from .base import *

urlpatterns += (
    [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
