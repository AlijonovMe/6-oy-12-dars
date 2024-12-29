from django.shortcuts import render, redirect, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from datetime import datetime
from .models import *
from .forms import *


def index(request):
    courses = Course.objects.all()
    lessons = Lessons.objects.all()

    context = {
        'courses': courses,
        'lessons': lessons,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def courses(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lessons.objects.filter(course_id=course_id)

    context = {
        'courses': [course],
        'lessons': lessons,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def lessons(request, lesson_id):
    lesson = get_object_or_404(Lessons, id=lesson_id)
    comments = Comment.objects.filter(lesson_id=lesson_id)

    context = {
        'lesson': lesson,
        'form': CommentForm(),
        'comments': comments,
        'current_year': datetime.now().year
    }

    return render(request, 'detail.html', context)


def comment_save(request: WSGIRequest, lesson_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            lesson = get_object_or_404(Lessons, pk=lesson_id)
            if form.is_valid():
                form.save(Comment, request.user, lesson)

                messages.success(request, "Izoh muvaffaqiyatli qo'shildi.")
                return redirect('lessons_detail', lesson_id=lesson_id)
    else:
        messages.error(request, "Iltimos, tizimga kirishingiz kerak.")
        return redirect('login')


def comment_delete(request: WSGIRequest, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user == comment.author or request.user.is_superuser:
            lesson_id = comment.lesson.id
            comment.delete()
            messages.success(request, "Izoh muvaffaqiyatli o'chirildi!")
            return redirect('lessons_detail', lesson_id=lesson_id)


def comment_update(request: WSGIRequest, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)
        lesson_id = comment.lesson.id
        if request.user == comment.author or request.user.is_superuser:
            if request.method == 'POST':
                form = CommentForm(data=request.POST)
                if form.is_valid():
                    form.update(comment)

                    messages.success(request, "Izoh muvaffaqiyatli o'zgartirildi.")
                    return redirect('lessons_detail', lesson_id=lesson_id)

            else:
                form = CommentForm(initial={'text': comment.text})

            context = {
                'lesson': comment.lesson,
                'form': form,
                'update': True,
                'comment': comment,
                'comments': Comment.objects.filter(lesson_id=lesson_id)
            }

            return render(request, 'detail.html', context)

    else:
        messages.error(request, "Iltimos, tizimga kirishingiz kerak.")
        return redirect('login')


def addCourse(request: WSGIRequest):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CourseForms(data=request.POST, files=request.FILES)
            if form.is_valid():
                print(form.cleaned_data)
                Course.objects.create(**form.cleaned_data)
                messages.success(request, "Ma'lumot muvaffaqiyatli qo'shildi.")
                return redirect('home')
        else:
            form = CourseForms()

        context = {
            'forms': form,
            'current_year': datetime.now().year
        }

        return render(request, 'addCourse.html', context)


def addLesson(request: WSGIRequest):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = LessonForms(data=request.POST, files=request.FILES)
            if form.is_valid():
                if Lessons.objects.filter(name=form.cleaned_data.get('name'),
                                          course=form.cleaned_data.get('course')).exists():
                    messages.error(request, "Ma'lumot qo'shilmadi.Bunday ma'lumot allaqachon qo'shilgan!")
                else:
                    Lessons.objects.create(**form.cleaned_data)
                    messages.success(request, "Ma'lumotlar muvaffaqiyatli qo'shildi.")
                return redirect('home')
        else:
            form = LessonForms()

        context = {
            'forms': form,
            'current_year': datetime.now().year
        }

        return render(request, 'addLesson.html', context)


def updateCourse(request: WSGIRequest, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.user.is_superuser:
        if request.method == 'POST':
            form = CourseForms(data=request.POST, files=request.FILES)

            if form.is_valid():
                if Course.objects.filter(name=form.cleaned_data.get('name')).exists():
                    messages.error(request, "Ma'lumot o'zgartirilmadi. Bunday ma'lumot allaqachon qo'shilgan!")
                    return redirect('home')

                form.update(course)

                messages.success(request, "Ma'lumot muvaffaqiyatli o'zgartirildi.")
                return redirect('home')

        else:
            form = CourseForms(initial={
                'name': course.name
            })

        context = {
            'forms': form,
            'current_year': datetime.now().year
        }

        return render(request, 'addLesson.html', context)


def deleteCourse(request, course_id):
    if request.user.is_superuser:
        course = get_object_or_404(Course, pk=course_id)
        course.delete()
        messages.success(request, "Ma'lumot muvaffaqiyatli o'chirildi.")
        return redirect('home')


def updateLesson(request: WSGIRequest, lesson_id):
    lesson = get_object_or_404(Lessons, pk=lesson_id)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = LessonForms(data=request.POST, files=request.FILES)
            if form.is_valid():
                form.update(lesson)

                messages.success(request, "Ma'lumot muvaffaqiyatli o'zgartirildi.")
                return redirect('lessons_detail', lesson_id=lesson_id)

        else:

            form = LessonForms(initial={
                'name': lesson.name,
                'homework': lesson.homework,
                'deadline': lesson.deadline,
                'course': lesson.course
            })

        context = {
            'forms': form,
            'current_year': datetime.now().year
        }

        return render(request, 'addLesson.html', context)


def deleteLesson(request, lesson_id):
    if request.user.is_superuser:
        lesson = get_object_or_404(Lessons, pk=lesson_id)
        lesson.delete()
        messages.success(request, "Ma'lumot muvaffaqiyatli o'chirildi.")
        return redirect('home')


def register(request: WSGIRequest):
    if request.method == 'POST':
        form = Register(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User.objects.create_user(username, email, password)

            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = Register()

    context = {
        'forms': form,
        'current_year': datetime.now().year
    }

    return render(request, 'auth/sign-up.html', context)


def loginPage(request: WSGIRequest):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
                return redirect('home')
            else:
                messages.error(request,
                               "Kiritilgan foydalanuvchi nomi yoki parol noto‘g‘ri. Iltimos, qayta tekshirib ko‘ring.")

    context = {
        'forms': LoginForm(),
        'current_year': datetime.now().year
    }

    return render(request, 'auth/login.html', context)


def logoutPage(request: WSGIRequest):
    logout(request)
    messages.success(request, "Tizimdan muvaffaqiyatli chiqdingiz!")
    return redirect('home')
