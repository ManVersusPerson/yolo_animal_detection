from ultralytics import YOLO
from typing import BinaryIO
from file_utils import convert_file_to_image

model = YOLO('model/model.pt')


class Model():
    def __init__(self, image_buf: BinaryIO):
        image = convert_file_to_image(image_buf.read())
        self.predicted_result = model.predict(image)[0]

    def get_predicred_result(self):
        return self.predicted_result