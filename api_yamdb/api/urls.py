from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UsersViewSet, get_confirmation_code, get_jwt_token
from .views import CategoryViewSet, GenreViewSet, TitleViewSet


router_v1 = DefaultRouter()
router_v1.register('users', UsersViewSet, basename='users')

router_v1.register("category", CategoryViewSet, basename="category")
router_v1.register("genre", GenreViewSet, basename="genre")
router_v1.register("title/<int:title_id>", TitleViewSet, basename="title")


v1_auth_patterns = [
    path('signup/', get_confirmation_code),
    path('token/', get_jwt_token),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include(v1_auth_patterns)),
]
