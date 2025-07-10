import qrcode
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
import base64

def generate_qr(request):
    # Get the URL from query parameters
    url = request.GET.get('url', 'https://example.com')  # Default to example.com if no URL provided

    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Save the QR code to a BytesIO stream
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    # Encode the image as a base64 string for embedding in HTML
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render(request, 'qr_code.html', {'qr_code': qr_code_base64, 'url': url})
