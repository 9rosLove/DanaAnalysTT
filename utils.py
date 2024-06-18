import gspread
import pandas as pd
from google.oauth2.service_account import Credentials


def authenticate(scopes: list, credentials: str) -> gspread.Client:
    credentials = Credentials.from_service_account_file(
        filename=credentials,
        scopes=scopes
    )
    client = gspread.authorize(credentials)

    return client


def write_to_worksheet(
        worksheet: gspread.Worksheet,
        df: pd.DataFrame,
        overwrite: bool = False
) -> None:
    if overwrite:
        worksheet.clear()

    worksheet.update([df.columns.values.tolist()] + df.values.tolist())


def create_spreadsheet(gclient: gspread.Client, title: str) -> gspread.Spreadsheet:
    return gclient.create(title)


def share_spreadsheet(spreadsheet: gspread.Spreadsheet, email: str):
    spreadsheet.share(email, perm_type="user", role="writer")


def create_worksheet(
        spreadsheet: gspread.Spreadsheet,
        title: str,
        rows: int,
        cols: int
) -> gspread.Worksheet:
    return spreadsheet.add_worksheet(title=title, rows=rows, cols=cols)


def add_worksheet_and_write_data(
        spreadsheet: gspread.Spreadsheet,
        df: pd.DataFrame,
        sheet_name: str) -> None:
    worksheet = spreadsheet.add_worksheet(
        title=sheet_name,
        rows=df.shape[0] + 1,
        cols=df.shape[1]
    )
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
