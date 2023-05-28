from file_utils import convert_image_to_bytes
import cv2
import uuid

IMG_EXTENSION = '.jpg'
IMAGES_PATH = 'localhost:8000/image/'


class Dilivery():
    def __init__(self, predicted_result):
        self.predicted_result = predicted_result

    def get_img_as_file(self, extension):
        image_buf = convert_image_to_bytes(
            self.predicted_result.plot(),
            extension)

        return image_buf

    def get_img_info_as_json(self):
        img_id = f'{uuid.uuid4()}'
        names = self.get_names()
        cv2.imwrite(
            f'output_images/{img_id}{IMG_EXTENSION}',
            self.predicted_result.plot())

        return {
            'img_url': IMAGES_PATH + img_id,
            'detected_objects': names
         }

    def get_names(self):
        result = {}

        for index in range(len(self.predicted_result.boxes)):
            box = int(self.predicted_result.boxes.cls[index])
            name = self.predicted_result.names[box]
            result[name] = result.get(name, 0) + 1

        return result
