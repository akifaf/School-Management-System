from django.shortcuts import render, HttpResponse
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from rest_framework import generics
from .models import User, Student, Teacher, ClassRoom, Subject
from .serializers import UserSerializer, StudentSerializer, TeacherSerializer, ClassroomSerializer, SubjectSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['is_admin'] = user.is_admin
        token['is_student'] = user.is_student
        token['is_teacher'] = user.is_teacher

        return token
        
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
   
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentRegisterView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherRegisterView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

class TeacherList(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

class ClassRoomAPIView(generics.ListCreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


