from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from .routes import ROUTES
from model.model import Model
from file_utils import extract_file_extension
from delivery import Dilivery

app = FastAPI()


# Initialize api app
@app.post(ROUTES['file_mode'])
def get_img_file(file: UploadFile):
    file_extension = extract_file_extension(file.filename)
    file_buf = file.file

    predicted_result = Model(file_buf).get_predicted_result()
    delivery_result = Dilivery(predicted_result) \
        .get_img_as_file(file_extension)

    return StreamingResponse((delivery_result), media_type="image/png")


@app.post(ROUTES['json_mode'])
def get_json_with_names(file: UploadFile):
    file_buf = file.file

    predicted_result = Model(file_buf).get_predicted_result()
    delivery_result = Dilivery(predicted_result).get_img_info_as_json()

    return delivery_result


@app.get(ROUTES['image'])
def get_image(id: str):
    return FileResponse(f'output_images/{id}.jpg', media_type="image/jpg")
