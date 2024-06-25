
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
    path('block-user/<int:pk>/', BlockUserView.as_view(), name='block-user'),
    path('unblock-user/<int:pk>/', UnBlockUserView.as_view(), name='block-user'),

    path('students/', StudentList.as_view(), name='students'),
    path('student-register/', StudentRegisterView.as_view(), name='student-register'),
    path('student-update/<int:pk>/', StudentListUpdateView.as_view(), name='student-update'),

    path('teacher-register/', TeacherRegisterView.as_view(), name='teacher-register'),
    path('teacher/', TeacherList.as_view(), name='teacher'),
    path('teacher-update/<int:pk>/', TeacherListUpdateView.as_view(), name='teacher-update'),
    
    # path('subject/', SubjectView.as_view(), name='subject'),
    path('subject/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subject/<int:pk>/', SubjectUpdateView.as_view(), name='subject-detail'),



    path('classroom/', ClassRoomAPIView.as_view(), name='classroom'),
]