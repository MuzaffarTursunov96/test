from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('teacherclick', views.teacherclick_view),
path('teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'),name='teacherlogin'),
path('teachersignup', views.teacher_signup_view,name='teachersignup'),
path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),
path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),


path('teacher-question', views.teacher_question_view,name='teacher-question'),
path('teacher-check-answers', views.teacher_check_answer,name='teacher-check-answer'),
path('teacher-set-mark/<int:pk>', views.teacher_set_mark,name='teacher-set-mark'),

path('teacher-add-question-file', views.teacher_question_file_view,name='teacher-question-file'),
path('teacher-add-question', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),
path('teacher-view-question-file', views.teacher_view_question_view_file,name='teacher-view-question-file'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('see-question-file/<int:pk>', views.see_question_view_file,name='see-question-file'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
path('remove-question-file/<int:pk>', views.remove_question_view_file,name='remove-question-file'),
]