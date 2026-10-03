import requests

BASE = "https://reqres.in/api"

def test_get_user_returns_200():
    response = requests.get(f"{BASE}/users/2")
    
    assert response.status_code == 200
   
  #test if data is corrrect  
def test_get_user_returns_correct_data():
    response = requests.get(f"{BASE}/users/2")
    data = response.json()

    
    assert data["data"]["id"] == 2
    assert "@" in data["data"]["email"]
    
# test if ther is a 404 error
def test_nonexistent_user_returns_404():
    response = requests.get(f"{BASE}/users/23")

    assert response.status_code == 404