# serializers.py
from rest_framework import serializers
from .models import User, Student, Teacher, ClassRoom, Subject

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'date_of_birth', 'address', 'phone_number', 'profile_picture', 'is_student', 'is_teacher', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class ClassroomSerializer(serializers.ModelSerializer):

    # teacher = TeacherSerializer()

    class Meta:
        model = ClassRoom
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class_room = ClassroomSerializer
    class Meta:
        model = Student
        fields = ['user', 'admission_date', 'parent_contact', 'class_room', 'roll_no']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password', None)
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        if password:
            user.set_password(password)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user, **validated_data)
        return student

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'subject', 'joined_date']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)
        user.is_teacher = True
        return teacher

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'