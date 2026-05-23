import csv
import json
import os

from openpyxl import Workbook
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib import colors
from reportlab.lib.styles import  getSampleStyleSheet


from gui.components.toast import Toast
from utils.storage import load_data
from utils.logger import (
    log_error,
    log_info
)

EXPORT_FOLDER = "exports"

def initialize_export_folder():
    """
    Create export folder if missing...
    """

    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)

def open_export_folder():
    os.startfile(EXPORT_FOLDER)


def export_to_csv(filename="expenses_export.csv"):
    """
    Export data to a CSV file.
    """

    try:
        initialize_export_folder()

        data = load_data()

        if not data:
            return False, "No expense data found."
        
        file_path = os.path.join(
            EXPORT_FOLDER,
            filename
        )

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=data[0].keys()
            )
            writer.writeheader()
            writer.writerows(data)
        
        log_info(f"CSV Exported: {file_path}")

        return True, file_path
    
    except Exception as error:
        log_error(f"CSV Exportation Error: {error}")
        return False, str(error)

def export_to_json(filename="expenses_export.json"):
    """
    Export data to a JSON file.
    """

    try:
        initialize_export_folder()

        data = load_data()

        if not data:
            return False, "No expense data found."

        file_path = os.path.join(
            EXPORT_FOLDER,
            filename
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as json_file:
            json.dump(data, json_file, indent=4)

        log_info(f"JSON Exported: {file_path}")
        return True, file_path

    except Exception as error:
        log_error(f"JSON Exportation Error: {error}")
        return False, str(error)

def export_to_excel(filename="expenses_export.xlsx"):
    """
    Export expenses to Excel file...
    """

    try:
        initialize_export_folder()
        
        data = load_data()

        if not data:
            return False, "No expense data found."
        
        file_path = os.path.join(
            EXPORT_FOLDER,
            filename
        )

        workbook = Workbook()

        sheet = workbook.active

        sheet.title = "Expenses"

        # Add headers
        headers = list(data[0].keys())

        sheet.append(headers)

        # Add rows
        for expense in data:

            sheet.append(list(expense.values()))

        workbook.save(file_path)
        log_info(f"Excel Exported: {file_path}")
        return True, file_path
    
    except Exception as error:
        log_error(f"Excel Exportation Error: {error}")
        return False, str(error)

def export_to_pdf(filename="expenses_export.pdf"):
    """
    Export expenses to PDF file...
    """

    try:
        initialize_export_folder()

        data = load_data()

        if not data:
            return False, "No expense data found."
        
        file_path = os.path.join(
            EXPORT_FOLDER,
            filename
        )

        document = SimpleDocTemplate(file_path)

        elements = []

        styles = getSampleStyleSheet()

        title = Paragraph(
            "Expense Report",
            styles["Title"]
        )

        elements.append(title)
        elements.append(Spacer(1, 12))

        # Table data
        table_data = []

        headers = list(data[0].keys())

        table_data.append(headers)

        for expense in data:
            table_data.append(
                list(expense.values())
            )

        table = Table(table_data)

        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0,0), (-1,0), colors.grey),
                    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
                    ("GRID", (0,0), (-1,-1), 1, colors.black),
                    ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold")
                ]
            )
        )

        elements.append(table)

        document.build(elements)

        log_info(f"PDF Exported: {file_path}")
        return True, file_path
    
    except Exception as error:
        log_error(f"PDF Exportation Error: {error}")
        return False, str(error)
    

