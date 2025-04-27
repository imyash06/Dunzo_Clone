from django.db import models

class forgotpassword(models.Model):
    student_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    standard = models.CharField(max_length=10)
    division = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=10)


