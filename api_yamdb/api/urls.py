from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import (
    UsersViewSet,
    get_confirmation_code,
    get_jwt_token
)
from .views import (
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    CommentViewSet,
    ReviewViewSet,
)


router_v1 = DefaultRouter()
router_v1.register('users', UsersViewSet, basename='users')
router_v1.register("titles", TitleViewSet, basename="titles")
router_v1.register("categories", CategoryViewSet, basename="categories")
router_v1.register("genres", GenreViewSet, basename="genres")
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews",
    ReviewViewSet,
    basename="reviews"
)
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename="comments",
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', get_confirmation_code),
    path('v1/auth/token/', get_jwt_token),
]
