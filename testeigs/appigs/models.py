from django.db import models


class  Departments(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Collaborators(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    departments = models.ForeignKey(Departments, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
