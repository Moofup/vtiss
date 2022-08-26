from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, SAFE_METHODS

from lessons.models import Class, LearningActivity, Subject
from lessons.permissions import IsAdminOrReadOnly
from lessons.serializers import TeacherSerializer, ClassSerializer, UserSerializer, LearningActivitySerializer, \
    SubjectSerializer
from users.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().filter(is_teacher=True)
    serializer_class = TeacherSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsAdminOrReadOnly,)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = LearningActivity.objects.all()
    serializer_class = LearningActivitySerializer
    # permission_classes = (IsAdminOrReadOnly,)

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAdminOrReadOnly,)


