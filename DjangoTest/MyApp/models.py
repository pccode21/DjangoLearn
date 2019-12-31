from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=20, null=False)
    age = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.id, self.name, self.age
