import os

from dotenv import load_dotenv

load_dotenv()

SHEET_ID = os.getenv("SHEET_ID")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]
