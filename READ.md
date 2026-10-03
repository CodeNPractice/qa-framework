[![Tests](https://github.com/CodeNPractice/qa-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/CodeNPractice/qa-framework/actions/workflows/tests.yml)

# QA Framework

UI and API test automation built with Python, Playwright, and pytest.

## What it tests

UI tests cover login (valid and invalid) and add-to-cart flows on saucedemo.com.
API tests cover GET requests, response payload validation, and 404 handling against reqres.in.

## Running it

```bash
git clone https://github.com/CodeNPractice/qa-framework.git
cd qa-framework
python3 -m venv venv
source venv/bin/activate
pip install pytest playwright requests
playwright install chromium
pytest -v
```

## Structure

```
pages/          Page objects — one class per page, selectors live here
conftest.py     Shared fixtures: browser session and logged-in page
config.py       Base URL and credentials
test_login.py   UI tests
test_api.py     API tests
```

## Design decisions

**conftest.py:** This is used for removing any repetition instead of rewriting the same code, instead I made page and logged_in_page to log call whenever I needed to grab the page or log in. I used yield to guarantee the teardown even if a test fails so a failing test won't leave the browser hanging.

**pages/:** Pages creates two classes one for each page I was testing. The login page and the products page. It comes with functions that locate elements and perform actions in an organised way. This also allows me to only need to change one file when a UI element is changed in a page instead of every test that touches the page.

**test_login:** This tests if the login works properly as well as if a user is able to add items to their cart. For testing valid login and invalid login conftest login wasn't used because it's testing the login itself and not the conftest.py.

**test_api:**  This tests using the api, it requests user information to see if it's possible and if the information is correct. It also tests getting information from non existent users to see if it could trigger errors. 
## Next

Parallel execution, HTML reporting with screenshots on failure, Docker.