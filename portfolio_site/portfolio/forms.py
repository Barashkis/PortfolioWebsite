from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=50)
    email = forms.EmailField(label="Email", max_length=100)
    subject = forms.CharField(label="Тема", max_length=150)
    message = forms.CharField(label="Сообщение")
