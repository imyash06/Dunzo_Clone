from django.db import models
from .school import School

class StudentRegistration(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    student_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    standard = models.CharField(max_length=10)
    division = models.CharField(max_length=10)
    parent_phone = models.CharField(max_length=15)
    roll_no = models.CharField(max_length=100, default="")
    actual_password = models.CharField(max_length=100, default="")
    address = models.TextField()
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('username', 'school_id')  # Ensures unique combination of username and school_id

    def register(self):
        self.save()

    @staticmethod
    def get_student_by_user(username):
        try:
            return StudentRegistration.objects.get(username=username)
        except:
            return False

    def isExist(self):
        if StudentRegistration.objects.filter(username=self.username, school_id=self.school_id):
            return True
        return False
