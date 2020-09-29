from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('location', views.LocationView)
router.register('courses', views.CourseView)
router.register('students', views.StudentView)

urlpatterns = [
    path('', include(router.urls))
]
