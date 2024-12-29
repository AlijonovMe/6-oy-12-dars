from django import forms
from .models import *
from .validators import *


class TypeForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': "Nomini kiriting",
            'class': "form-control"
        }),
        label="",
        validators=[type_name]
    )


class FlowerForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': "Nomini kiriting",
            'class': "form-control"
        }),
        label=""
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': "Tavsifini kiriting",
            'class': "form-control"
        }),
        initial="Ma'lumot qo'shilmadi!",
        label="",
        required=False,
    )

    price = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={
            'placeholder': "Narxini kiriting",
            'class': "form-control"
        }),
        label=""
    )

    count = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={
            'placeholder': "Sonini kiriting",
            'class': "form-control"
        }),
        label=""
    )

    published = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': "form-check-input",
            'checked': "checked"
        }),
        label="Nashr etilgan",
        required=False
    )

    type = forms.ModelChoiceField(
        queryset=Types.objects.all(),
        widget=forms.Select(attrs={
            'class': "form-select"
        }),
        label=""
    )


class RegisterForm(forms.Form):
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
        label="Elektron pochta manzili"
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
        label="Foydalanuvchi nomi"
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

    def save(self, comment, user, flower):
        comment.objects.create(
            text=self.cleaned_data.get('text'),
            author=user,
            flower=flower
        )

    def update(self, value):
        value.text = self.cleaned_data.get('text')
        value.save()
