import os

from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
SHEET_ID = os.getenv("SHEET_ID")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
    ]
