import gspread
from google.oauth2.service_account import Credentials


def authenticate(scopes: list, credentials: str) -> gspread.Client:
    credentials = Credentials.from_service_account_file(
        filename=credentials, scopes=scopes
    )
    client = gspread.authorize(credentials)
    return client
