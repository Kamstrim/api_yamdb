from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

router = DefaultRouter()
router.register("category", CategoryViewSet, basename="category")
router.register("genre", GenreViewSet, basename="genre")
router.register("title/<int:title_id>", TitleViewSet, basename="title")
