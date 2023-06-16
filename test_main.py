from fastapi.testclient import TestClient
from api.api import app

client = TestClient(app)
test_filename = ("./img_test/Fish.jpg", "./img_test/Fox.jpg")
ROUTES = ('/predict/img', '/predict/json')


def test_upload_image():
    for filename in test_filename:
        for routes in ROUTES:
            files = {"file": (open(filename, "rb"))}
            response = client.post(
                routes, files=files)
            assert response.status_code == 200
