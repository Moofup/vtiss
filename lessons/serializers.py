from rest_framework import serializers

from lessons.models import Class, Subject
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'fullname',
            'qualification', 'is_teacher',
        )


class ClassSerializer(serializers.ModelSerializer):
    room_number = serializers.CharField(source='name')

    class Meta:
        model = Class
        fields = ('id', 'room_number',)


class SubjectSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='name')

    class Meta:
        model = Subject
        fields = ('id', 'subject_name',)


class TeacherSerializer(serializers.ModelSerializer):
    rooms = ClassSerializer(many=True)
    subjects = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'fullname', 'rooms', 'subjects')
