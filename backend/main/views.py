from django.shortcuts import render, HttpResponse
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from .models import User, Student, Teacher, ClassRoom, Subject
from .serializers import UserSerializer, StudentSerializer, TeacherSerializer, ClassroomSerializer, SubjectSerializer
from django.shortcuts import get_object_or_404

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



class StudentListUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer

    # def get(self, request, pk):
    #     student = get_object_or_404(Student, user_id=pk)
    #     serializer = self.get_serializer(student)
    #     return Response(serializer.data)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Student, user_id=pk)

    def put(self,request,*args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()
        password = data.get('password')
        if password:
            instance.set_password(password)
            instance.save()
            data.pop('password',None)
        serializer = self.get_serializer(instance,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User

@api_view(['PATCH'])
def block_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return Response({"message": "User blocked successfully"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH'])
def unblock_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.is_active = True
        user.save()
        return Response({"message": "User Activated"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


