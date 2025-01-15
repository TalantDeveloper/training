from training.settings import BASE_DIR, BASE_URL
import pyqrcode
import png


def create_qrcode(request, student_id):
    message = f"{BASE_URL}/uz/students/{student_id}"
    text = pyqrcode.create(message)
    text.png(f"{BASE_DIR}/media/student/{student_id}.png", scale=8)
    return f"{BASE_URL}/media/student/{student_id}.png"
