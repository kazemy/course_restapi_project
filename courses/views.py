from django.shortcuts import render
from rest_framework import viewsets
from .models import Location, Course, Student
from .serializers import LocationSerializer, CourseSerializer, StudentSerializer

class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
