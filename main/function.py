from training.settings import BASE_DIR
import pyqrcode
import png


def create_qrcode(request):
    message = f"https://tsdi.uz/rektorat"
    text = pyqrcode.create(message)
    text.png(f"{BASE_DIR}/media/student/123.png", scale=8)
    return "media/student/123.png"


