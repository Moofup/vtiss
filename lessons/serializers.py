from rest_framework import serializers

from lessons.models import Class, Subject, LearningActivity
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
        fields = ('room_number',)


class SubjectSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='name')

    class Meta:
        model = Subject
        fields = ('subject_name',)


class TeacherSerializer(serializers.ModelSerializer):
    rooms = ClassSerializer(many=True)
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = User
        fields = ('fullname', 'rooms', 'subjects')

    def create(self, validated_data):
        rooms = validated_data.pop('rooms')
        subjects = validated_data.pop('subjects')
        teacher = User.objects.create(**validated_data)
        for room, subject in rooms, subjects:
            print(room)
            print(subject)
            current_room, status = Class.objects.get_or_create(
                **room)
            current_subject, status = Subject.objects.get_or_create(
                **subject)
            LearningActivity.objects.create(rooms=current_room, teachers=teacher, subjects=current_subject)
        return teacher


class LearningActivitySerializer(serializers.ModelSerializer):
    teachers = serializers.PrimaryKeyRelatedField(read_only='True')
    class Meta:
        model = LearningActivity
        fields = ('__all__')

    # def validate(self, data):
    #     print(data)
    #     teacher = data['teachers']
    #     if not teacher['is_teacher']:
    #         raise serializers.ValidationError('Проверьте год рождения!')
    #     return data
