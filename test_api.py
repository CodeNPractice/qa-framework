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
    
def test_user_id_is_an_integer():
    response = requests.get(f"{BASE}/users/2")
    user_id = response.json()["data"]["id"]
    assert isinstance(user_id, int)
    
def test_response_under_one_second():
    response = requests.get(f"{BASE}/users/2")
    assert response.elapsed.total_seconds() < 1

def test_all_users_returns_a_list():
    response = requests.get(f"{BASE}/users")
    users = response.json()["data"]
    assert isinstance(users, list)
    assert len(users) > 0
    assert len(users) > 0
    
    
def test_create_user_returns_201():
    payload = {"name": "Abood", "job": "QA"}
    response = requests.post(f"{BASE}/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Abood"