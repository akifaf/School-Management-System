
from django.urls import path
from . import views
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user-register/', UserRegisterView.as_view(), name='user-register'),
    path('student-register/', StudentRegisterView.as_view(), name='student-register'),
    path('teacher-register/', TeacherRegisterView.as_view(), name='teacher-register'),

    path('students/', StudentList.as_view(), name='students'),
    path('teacher/', TeacherList.as_view(), name='teacher'),
    
    path('subject/', SubjectList.as_view(), name='subject'),

    path('classroom/', ClassRoomAPIView.as_view(), name='classroom'),
]