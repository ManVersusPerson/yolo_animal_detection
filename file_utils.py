import numpy as np
import cv2
import io
from PIL import Image


# Convert binary image to Image type
def convert_file_to_image(file_buf):
    img = cv2.imdecode(np.frombuffer(file_buf, np.uint8), cv2.IMREAD_COLOR)
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))


# Convert Image to binary type
def convert_image_to_bytes(image, img_extension):
    _, encoded = cv2.imencode('.' + img_extension, image)
    return io.BytesIO(encoded.tobytes())


# Extract file extension from filename string
def extract_file_extension(file: str):
    return file.split('.')[-1]
