from django import forms
from .models import *
from .validators import *

class CourseForms(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': "Nomini kiriting",
            'class': "form-control"
        }),
        label="",
        validators=[course_name],
    )

    def update(self, value):
        value.name = self.cleaned_data.get('name')
        value.save()


class LessonForms(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': "Nomini kiriting",
            'class': "form-control"
        }),
        label="",
        validators=[lesson_name],
    )

    homework = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': "Uyga vazifani kiriting",
            'class': "form-control"
        }),
        label="",
        validators=[homework_length],
    )

    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': "datetime-local"
        }),
        input_formats=['%d.%m.%Y %H:%M'],
        label="",
    )

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select({
            'class': "form-select"
        }),
        label="",
    )

    def update(self, value):
        value.name = self.cleaned_data.get('name')
        value.homework = self.cleaned_data.get('homework')
        value.deadline = self.cleaned_data.get('deadline') if self.cleaned_data.get(
            'deadline') else value.deadline
        value.course = self.cleaned_data.get('course')
        value.save()


class Register(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Foydalanuvchi nomi",
        validators=[user_valid]
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Elektron pochta manzili",
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Parol"
    )
    confirm_password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Parolni qayta kiriting"
    )


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Parollar bir-biriga mos kelmayapti. Iltimos, qayta tekshirib, to'g'ri kiriting!")

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Foydalanuvchi nomi",
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Parol"
    )


class CommentForm(forms.Form):
    text = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            'placeholder': "Izohingizni yozing...",
            'class': "form-control",
            'rows': 3,
            'style': 'resize: none;',
        }),
        label="Izoh matni",
    )

    def save(self, comment, user, lesson):
        comment.objects.create(
            text=self.cleaned_data.get('text'),
            author=user,
            lesson=lesson
        )

    def update(self, value):
        value.text = self.cleaned_data.get('text')
        value.save()
