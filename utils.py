import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from gspread import Worksheet


def authenticate(scopes: list, credentials: str) -> gspread.Client:
    credentials = Credentials.from_service_account_file(
        filename=credentials,
        scopes=scopes
    )
    client = gspread.authorize(credentials)

    return client


def write_to_worksheet(
        worksheet: Worksheet,
        df: pd.DataFrame,
        overwrite: bool = False
) -> None:
    if overwrite:
        worksheet.clear()

    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
