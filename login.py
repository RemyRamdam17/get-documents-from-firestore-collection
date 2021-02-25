import json
import requests
from requests.exceptions import HTTPError

FIREBASE_REST_API = "https://identitytoolkit.googleapis.com/v1/accounts"

# Use the google verify password REST api to authenticate and generate user tokens
def sign_in_with_email_and_password(api_key, email, password):
    request_url = "%s:signInWithPassword?key=%s" % (FIREBASE_REST_API, api_key)
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})

    resp = requests.post(request_url, headers=headers, data=data)
    # Check for errors
    try:
        resp.raise_for_status()
    except HTTPError as e:
        raise HTTPError(e, resp.text)

    return resp.json()
