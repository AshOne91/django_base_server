from django.contrib import admin
from django.urls import path
from test_app import views

# Swagger 관련 추가
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="Swagger 문서",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/login/", views.account_login, name="account_login"),
    path("account/block/", views.account_block, name="account_block"),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
