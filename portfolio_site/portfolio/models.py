from django.db import models


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Project(models.Model):
    title = models.CharField(max_length=125)
    excerpt = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to="img", null=True)
    tags = models.ManyToManyField(Tag)
    source = models.URLField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    job = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateField(blank=False)
    end = models.DateField(blank=False)

    def __str__(self):
        return f"{self.job} in {self.organization}"


class Education(models.Model):
    qualification = models.CharField(max_length=200)
    university_name = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateField(blank=False)
    end = models.DateField(blank=False)

    def __str__(self):
        return f"{self.qualification}, study in {self.university_name}"


class Skill(models.Model):
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill
