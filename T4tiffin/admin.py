from django.contrib import admin
from .models.students import StudentRegistration
from .models.standard import Standards
from .models.school import School
from .models.orders import Orders
from .models.qrcodes import Qrcodes
# # Register your models here.


admin.site.register(Standards)
admin.site.register(StudentRegistration)
admin.site.register(School)
admin.site.register(Orders)
admin.site.register(Qrcodes)
