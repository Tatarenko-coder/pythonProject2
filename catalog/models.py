from django.db import models


class Project(models.Model):
    project = models.CharField("Назва проекта", max_length=50)
    task_project = models.TextField("Про прект")
    working_hours = models.DateField("время над проектом",
                                      help_text='введите время над проектом', null=True,
                                     blank=True)

    def __str__(self):
        return self.project

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
