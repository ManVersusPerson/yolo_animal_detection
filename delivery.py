from file_utils import convert_image_to_bytes
import cv2
import uuid

IMG_EXTENSION = '.jpg'
IMAGES_PATH = 'localhost:8000/image/'


# Class for handling api requests
class Dilivery():
    def __init__(self, predicted_result):
        self.__predicted_result = predicted_result

    # Return the processed image in binary type response
    def get_img_as_file(self, extension):
        image_buf = convert_image_to_bytes(
            self.__predicted_result.plot(),
            extension)

        return image_buf

    # Return json response with detected names dict and link of processed image
    def get_img_info_as_json(self):
        img_id = f'{uuid.uuid4()}'
        names = self.__get_names()
        cv2.imwrite(
            f'output_images/{img_id}{IMG_EXTENSION}',
            self.__predicted_result.plot())

        return {
            'img_url': IMAGES_PATH + img_id,
            'detected_objects': names
         }

    # Helper method to get detected names dict
    def __get_names(self):
        result = {}

        for index in range(len(self.predicted_result.boxes)):
            box = int(self.predicted_result.boxes.cls[index])
            name = self.predicted_result.names[box]
            result[name] = result.get(name, 0) + 1

        return result
