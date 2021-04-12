from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
# from api.views import ExampleApiSet

router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'example', ExampleApiSet)

urlpatterns = [
    path('', include(router.urls + [
        re_path(r'^token/?$', jwt_views.TokenObtainPairView.as_view(),
                name='token_obtain_pair'),
        re_path(r'^token/refresh/?$',
                jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    ])),
    path('auth/', include('rest_framework.urls')),
]