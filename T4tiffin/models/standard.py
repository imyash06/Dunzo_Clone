from django.db import models
from .students import StudentRegistration

class Standards(models.Model):
    standard = models.CharField(max_length=10)
    username = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE)


    def info(self):

        self.save()