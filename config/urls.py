from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from user.views import CustomTokenObtainPairView, UserViewSet, StudentProfileViewSet
from hackathon.views.auth import forget_password, reset_password, validate_token

from hackathon.views import (
    AvailableStudentViewSet,
    SupporterViewSet,
    AvaliationViewSet,
    CriterionViewSet,
    ClassInfoViewSet,
    CourseViewSet,
    EditionViewSet,
    TeamViewSet,
    RankingViewSet,
    CategoryViewSet,
    approve_team,
    reject_team,
    ProjectViewSet,
)

router = DefaultRouter()

router.register("classes", ClassInfoViewSet)
router.register("courses", CourseViewSet)
router.register("supporters", SupporterViewSet)
router.register("avaliations", AvaliationViewSet)
router.register("criteria", CriterionViewSet)
router.register("editions", EditionViewSet)
router.register("teams", TeamViewSet)
router.register("rankings", RankingViewSet)
router.register("categories", CategoryViewSet)
router.register(
    "available-students", AvailableStudentViewSet, basename="available-students"
)
router.register("users", UserViewSet)
router.register("student-profiles", StudentProfileViewSet)
router.register("projects", ProjectViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("accept-team/<str:verification_token>/", approve_team, name="accept-team"),
    path("reject-work/<str:verification_token>/", reject_team, name="reject-team"),
    path("api/media/", include(uploader_router.urls)),
    path("api/forget-password/", forget_password, name="forget_password"),
    path("api/reset-password/", reset_password, name="reset_password"),
    path("api/validate-token/", validate_token, name="validate_token"),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
