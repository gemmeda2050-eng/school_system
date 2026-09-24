from django.db import models
from teachers.models import Teacher


class Class(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=50, blank=True)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    academic_year = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.section}"
