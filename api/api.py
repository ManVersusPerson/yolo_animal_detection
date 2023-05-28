from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from .routes import ROUTES
from model.model import Model
from file_utils import extract_file_extension
from delivery import Dilivery

app = FastAPI()


@app.post(ROUTES['file_mode'])
def get_img_file(file: UploadFile):
    file_extension = extract_file_extension(file.filename)
    file_buf = file.file

    predicted_result = Model(file_buf).get_predicred_result()
    delivery_result = Dilivery(predicted_result) \
        .get_img_as_file(file_extension)

    return StreamingResponse((delivery_result), media_type="image/jpg")
