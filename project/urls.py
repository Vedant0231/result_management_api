from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
"""install 'TokenObtainPairView', 'TokenVerifyView', 'TokenRefreshView'
for token creation, verification and new token refresh."""
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView 

""" this defaultrouter will help to perform curd opration with less effort."""
router = DefaultRouter()
router.register("student", views.Studentlist, basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("curd/",include(router.urls)),
    path("gettoken/",TokenObtainPairView.as_view(), name="token"),
    path("refreshtoken/", TokenRefreshView.as_view(),name= "token_refresh"),
    path("verifytoken/",TokenVerifyView.as_view(),name="token_verify")
]
