from google.oauth2.credentials import Credentials
from login import sign_in_with_email_and_password
from config import EMAIL, PASSWORD, API_KEY


# We use the sign_in_with_email_and_password function
response = sign_in_with_email_and_password(API_KEY, EMAIL, PASSWORD)
# Use google.oauth2.credentials and the response object to create the correct user credentials
creds = Credentials(response['idToken'], response['refreshToken'])