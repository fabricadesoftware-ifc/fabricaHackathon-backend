"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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

from hackathon.views import (
    StudentViewSet,
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
    ImagesViewSet,
    approve_team,
    reject_team,
)

router = DefaultRouter()

router.register("classes", ClassInfoViewSet)
router.register("courses", CourseViewSet)
router.register("students", StudentViewSet)
router.register("supporters", SupporterViewSet)
router.register("avaliations", AvaliationViewSet)
router.register("criteria", CriterionViewSet)
router.register("editions", EditionViewSet)
router.register("teams", TeamViewSet)
router.register("rankings", RankingViewSet)
router.register("categories", CategoryViewSet)
router.register("images", ImagesViewSet)
router.register("available-students", AvailableStudentViewSet, basename="available-students")
router.register("users", UserViewSet)
router.register("student-profiles", StudentProfileViewSet)

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
]
