from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from lessons.models import Class
from lessons.permissions import IsAdminOrReadOnly
from lessons.serializers import TeacherSerializer, ClassSerializer, UserSerializer, SubjectSerializer
from users.models import User

class UserViewSet(viewsets.ModelViewSet):
    """
    Вьююсет для работы с пользователями. Права на изменения записей есть только у администратора.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class TeacherViewSet(viewsets.ModelViewSet):
    """
    Возвращает список всех учителей.
    По id учителя возвращает все классы и предметы учителя.
    """
    queryset = User.objects.all().filter(is_teacher=True)
    serializer_class = TeacherSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ClassViewSet(viewsets.ModelViewSet):
    """
    Возвращает список помещений. Администратор может добавлять/изменять/удалять записи.
    """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsAdminOrReadOnly,)
