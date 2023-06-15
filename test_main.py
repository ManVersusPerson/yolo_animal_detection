from fastapi.testclient import TestClient
from api.api import app

client = TestClient(app)


def test_upload_image_file_mode():
    filename = "./img_test/Fish.jpg"
    files = {"file": (open(filename, "rb"))}
    response = client.post(
        "/predict/img", files=files)
    assert response.status_code == 200


def test_upload_image_json_mode():
    filename = "./img_test/Fox.jpg"
    files = {"file": (open(filename, "rb"))}
    response = client.post(
        "/predict/json", files=files)
    assert response.status_code == 200


