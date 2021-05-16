from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register(r"person", views.PersonViewSet, basename="person")
router.register(r"place", views.PlaceViewSet, basename="place")
router.register(r"picture", views.PictureViewSet, basename="picture")
urlpatterns = router.urls
