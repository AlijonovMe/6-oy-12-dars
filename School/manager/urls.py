from django.urls import path
from .views import *

urlpatterns = [
    # main home
    path('', index, name='home'),

    # course
    path('course/<int:course_id>/', courses, name='courses_detail'),
    path('course/add/', addCourse, name='addCourse'),
    path('course/<int:course_id>/update/', updateCourse, name='updateCourse'),
    path('course/<int:course_id>/delete/', deleteCourse, name='deleteCourse'),

    # lessons
    path('lesson/<int:lesson_id>/', lessons, name='lessons_detail'),
    path('lesson/add/', addLesson, name='addLesson'),
    path('lesson/<int:lesson_id>/update/', updateLesson, name='updateLesson'),
    path('lesson/<int:lesson_id>/delete/', deleteLesson, name='deleteLesson'),

    # comment
    path('lesson/<int:lesson_id>/comment/save/', comment_save, name='comment_save'),
    path('comment/<int:comment_id>/delete/', comment_delete, name='deleteComment'),
    path('comment/<int:comment_id>/update/', comment_update, name='updateComment'),

    # auth
    path('auth/register/', register, name='register'),
    path('auth/login/', loginPage, name='login'),
    path('auth/logout/', logoutPage, name='logout')

]
