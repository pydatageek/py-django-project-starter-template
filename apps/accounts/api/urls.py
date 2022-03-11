from django.urls import include, path

from rest_framework import routers

from .views import UserView, GroupView

router = routers.DefaultRouter()
router.register("users", UserView)
router.register("groups", GroupView)

urlpatterns = [
    path("", include(router.urls)),
]
