from django.db import models
from .students import StudentRegistration
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

class Qrcodes(models.Model):
    username = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE)
    parmanantqr = models.ImageField(upload_to='qr_codes/', blank=True)
    multiple = models.ImageField(upload_to='ml_qrcodes/', blank=True)
    encrypt1 = models.CharField(max_length=500)
    encrypt2 = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        # Helper function to generate QR code with logo
        def generate_qr_with_logo(data, logo_path, output_filename):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            # Create QR code image
            qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            # Open logo
            try:
                logo = Image.open(logo_path)
                print("Logo loaded successfully.")
            except Exception as e:
                print(f"Error loading logo: {e}")
                return None

            # Resize logo to 50% of QR code size
            qr_width, qr_height = qr_img.size
            logo_size = int(qr_width * 0.8)  # 50% of QR code size
            logo = logo.resize((logo_size, logo_size))

            # Calculate position for the logo
            pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

            # Paste logo onto QR code
            qr_img.paste(logo, pos, mask=logo)

            # Save QR code with logo
            buffer = BytesIO()
            qr_img.save(buffer, format="PNG")
            buffer.seek(0)
            return File(buffer, name=output_filename)

        # Permanent QR code with logo
        logo_path = "media/images/qrlogo.png"  # Update path as per your project
        self.parmanantqr = generate_qr_with_logo(self.encrypt1, logo_path, f'{self.username.username}_qr.png')

        # Multiple QR code with logo
        self.multiple = generate_qr_with_logo(self.encrypt2, logo_path, f'{self.username.username}_qr_multiple.png')

        super().save(*args, **kwargs)
