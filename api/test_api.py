from api.api_client import APIClient

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    api = APIClient(BASE_URL)
    response = api.get("/posts")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_post():
    api = APIClient(BASE_URL)

    payload = {
        "title": "Test",
        "body": "Automation",
        "userId": 1
    }

    response = api.post("/posts", payload)

    assert response.status_code == 201
    assert response.json()["title"] == "Test"