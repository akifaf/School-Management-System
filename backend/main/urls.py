
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
    path('block-user/<int:pk>/', views.block_user, name='block-user'),
    path('unblock-user/<int:pk>/', views.unblock_user, name='unblock-user'),

    path('students/', StudentList.as_view(), name='students'),
    # path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student-register/', StudentRegisterView.as_view(), name='student-register'),
    path('student-update/<int:pk>/', StudentListUpdateView.as_view(), name='student-update'),

    path('teacher-register/', TeacherRegisterView.as_view(), name='teacher-register'),
    path('teacher/', TeacherList.as_view(), name='teacher'),
    
    path('subject/', SubjectList.as_view(), name='subject'),

    path('classroom/', ClassRoomAPIView.as_view(), name='classroom'),
]