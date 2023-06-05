from ultralytics import YOLO
from typing import BinaryIO
from file_utils import convert_file_to_image

model = YOLO('model/model.pt')


# Class for work with YOLO model
class Model():
    def __init__(self, image_buf: BinaryIO):
        image = convert_file_to_image(image_buf.read())
        self.__predicted_result = model.predict(image)[0]

    # Return prdicted result
    def get_predicted_result(self):
        return self.__predicted_result
