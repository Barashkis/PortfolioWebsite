from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import Project, Skill, Education, WorkExperience
from .forms import ContactForm


def index(request):
    projects = Project.objects.all().order_by("-id")[:3]

    return render(request, "portfolio/index.html", context={
        "projects": projects
    })


def project_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    last_tag = project.tags.latest("id")

    return render(request, "portfolio/project_details.html", {
        "project": project,
        "last_tag": last_tag
    })


def about_me(request):
    return render(request, "portfolio/about_me.html", {
        "skills": Skill.objects.all(),
        "workings": WorkExperience.objects.all(),
        "educations": Education.objects.all()
    })


class ContactMe(View):
    @staticmethod
    def get(request):
        contact_form = ContactForm()

        return render(request, 'portfolio/contact.html', {
            'contact_form': contact_form
        })

    @staticmethod
    def post(request):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            message += f"\nПочта отправителя: {from_email}"

            try:
                send_mail(subject, message, from_email, ['testpost04@gmail.com'])
            except BadHeaderError:
                return render(request, "404.html")

            return render(request, "portfolio/contact.html", {
                'name': name,
            })

        return render(request, "portfolio/contact.html", {
            'contact_form': contact_form
        })


class ShowProjects(ListView):
    template_name = "portfolio/project_list.html"
    model = Project
    ordering = ["-id"]
    context_object_name = "projects"
