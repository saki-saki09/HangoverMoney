import tkinter as tk
from tkinter import ttk

from gui.styles import *
from gui.components.toast import Toast

from modules.add_expense import add_expense

class AddExpensePage:
    def __init__(
        self,
        parent,
        dashboard_page
    ):
        self.theme = get_theme()
        self.frame = tk.Frame(
            parent,
            bg = self.theme["content"]
        )
        self.dashboard_page = dashboard_page
        self.setup_ui()
    
    # ------------------------------------

    def setup_ui(self):
        title = tk.Label(
            self.frame,
            text = "Add Expense",
            bg = self.theme["content"],
            fg = self.theme["text"],
            font= TITLE_FONT
        )

        title.pack(pady=20)

        # Amount
        self.amount_label = tk.Label(
            self.frame,
            text = "Amount:",
            bg = self.theme["content"],
            fg = self.theme["text"],
            font= NORMAL_FONT
        )
        self.amount_label.pack(pady=10)
        self.amount_entry = tk.Entry(
            self.frame,
            font= NORMAL_FONT
        )

        self.amount_entry.pack(pady=10)

        # Category
        self.category_label = tk.Label(
            self.frame,
            text = "Category:",
            bg = self.theme["content"],
            fg = self.theme["text"],
            font= NORMAL_FONT
        )
        self.category_label.pack(pady=10)
        self.category_dropdown = ttk.Combobox(
            self.frame,
            values=[
                "Food",
                "Transport",
                "Shopping",
                "Bills",
                "Entertainment",
                "Health",
                "Education",
                "Travel",
                "Other"
            ],
            state="readonly"
        )
        self.category_dropdown.pack(pady=10)

        # Note
        self.note_label = tk.Label(
            self.frame,
            text = "Note:",
            bg = self.theme["content"],
            fg = self.theme["text"],
            font= NORMAL_FONT
        )
        self.note_label.pack(pady=10)
        self.note_entry = tk.Entry(
            self.frame,
            font=NORMAL_FONT
        )
        self.note_entry.pack(pady=10)

        # Add Button
        add_button = tk.Button(
            self.frame,
            text = "Add Expense",
            bg = self.theme["accent"],
            fg= self.theme["text"],
            font=BUTTON_FONT,
            command=self.submit_expense
        )
        add_button.pack(
            pady=20
        )

    # ----------------------------------------

    def submit_expense(self):
        amount = self.amount_entry.get()
        category = self.category_dropdown.get()
        note = self.note_entry.get()

        success, result = add_expense(
            amount,
            category,
            note
        )

        if success:
            Toast(self.frame, "✅ Expense added successfully.")

            # Auto refresh dashboard
            self.dashboard_page.refresh_data()

            self.amount_entry.delete(0, tk.END)
            self.category_dropdown.set("")
            self.note_entry.delete(0, tk.END)
        else:
            Toast(self.frame, "❌ Failed to add expense.")
