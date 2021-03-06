from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('student_upload/',views.student_upload, name="student_upload"),
    path('teacher_upload/', views.teacher_upload, name='teacher_upload'),
    path('success/', views.index, name='success'),
    path('', views.index, name='index'),
    path('homework_list', views.homework_list, name='homework_list'),
    path('homework_detail/<int:pk>/', views.student_upload, name='student_upload'),
    path('teacher_homework_list/', views.teacher_homeworks_list, name='teacher_home_work_list'),
    path('download_student_answers/<int:pk>', views.download_student_answers, name="download_student_answers"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)