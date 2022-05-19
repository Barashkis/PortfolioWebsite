from django.contrib import admin
from .models import Tag, Project, Education, WorkExperience, Skill


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("date", "tags",)
    list_display = ("title", "date",)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Skill)
