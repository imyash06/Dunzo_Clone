from django.db import models

class School(models.Model):
    school_id = models.CharField(max_length=50, unique=True, default="")  # Add this field
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')
    contact = models.CharField(max_length=10, default='')
    address = models.CharField(max_length=100, default='')

    @staticmethod
    def get_school_by_user(username):
        try:
            return School.objects.get(username=username)
        except:
            return False
