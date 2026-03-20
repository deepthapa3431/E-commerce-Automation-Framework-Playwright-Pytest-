from api.api_client import APIClient
from config.config import BASE_URL

def test_create_user_and_use_in_ui(page):
    api = APIClient("https://jsonplaceholder.typicode.com")

    # Step 1: Create user via API
    payload = {
        "name": "TestUser",
        "username": "testuser123",
        "email": "test@example.com"
    }

    response = api.create_user(payload)
    assert response.status_code == 201

    user = response.json()

    # Step 2: Use in YOUR UI (SauceDemo)
    page.goto(BASE_URL)

    # Example: use API data in login (simulation)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Just demonstrate usage of API data
    assert user["name"] == "TestUser"