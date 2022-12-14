from django.urls import path, include
from rest_framework.routers import DefaultRouter

from lessons.views import UserViewSet, TeacherViewSet, ClassViewSet

app_name = 'lessons'

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('teachers', TeacherViewSet)
router.register('rooms', ClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
