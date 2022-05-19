from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("projects", views.ShowProjects.as_view(), name="projects"),
    path("contact", views.ContactMe.as_view(), name="contact"),
    path("about-me", views.about_me, name="about-me"),
    path("<slug:slug>", views.project_details, name="project_details")
]
