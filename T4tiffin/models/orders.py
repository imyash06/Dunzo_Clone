from django.db import models
from .students import StudentRegistration
import qrcode
from io import BytesIO
from django.core.files import File



class Orders(models.Model):

    STATUS_CHOICES =[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    username = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    additional_note = models.CharField(max_length=100,default=None)
    order_status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending')
    code = models.CharField(max_length=5, default="")
    encrypt = models.CharField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank = True)


    def save(self, *args, **kwargs):
        # QR Code Generate
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_data = f'encrypt: {self.encrypt} '
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Save QR Code Image
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Save to ImageField
        self.qr_code.save(f'{self.username}_qr.png', File(buffer), save=False)
        super().save(*args, **kwargs)


    
    def ord(self):

        self.save()