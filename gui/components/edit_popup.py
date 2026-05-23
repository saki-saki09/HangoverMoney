import tkinter as tk

from tkinter import messagebox

from gui.components.toast import Toast

from gui.styles import *

from modules.edit_expense import (
    edit_expense
)

from modules.delete_expense import (
    delete_expense
)


class EditPopup:

    def __init__(
        self,
        parent,
        expense_data,
        refresh_callback
    ):
        
        self.parent = parent

        self.theme = get_theme()
        self.expense_data = expense_data

        self.refresh_callback = (
            refresh_callback
        )

        # Create popup window
        self.window = tk.Toplevel(parent)

        self.window.iconbitmap(
            "assets/logo.ico"
        )

        self.window.title("Edit Expense")

        self.window.geometry("400x350")

        self.window.configure(
            bg=self.theme["content"]
        )

        self.setup_ui()

    # -------------------------------------------------

    def setup_ui(self):

        title = tk.Label(
            self.window,
            text="Edit Expense",
            bg=self.theme["content"],
            fg=self.theme["text"],
            font=TITLE_FONT
        )

        title.pack(pady=20)

        # ---------------------------
        # Amount
        # ---------------------------

        amount_label = tk.Label(
            self.window,
            text="Amount",
            bg=self.theme["content"],
            fg=self.theme["text"]
        )

        amount_label.pack()

        self.amount_entry = tk.Entry(
            self.window
        )

        self.amount_entry.pack(pady=5)

        self.amount_entry.insert(
            0,
            self.expense_data["amount"]
        )

        # ---------------------------
        # Category
        # ---------------------------

        category_label = tk.Label(
            self.window,
            text="Category",
            bg=self.theme["content"],
            fg=self.theme["text"]
        )

        category_label.pack()

        categories = [
            "Food",
            "Transport",
            "Shopping",
            "Bills",
            "Entertainment",
            "Health",
            "Education",
            "Travel",
            "Other"
        ]

        self.category_dropdown = tk.OptionMenu(
            self.window,
            tk.StringVar(value=self.expense_data["category"]),
            *categories
        )

        self.category_dropdown.pack(pady=5)
        # ---------------------------
        # Note
        # ---------------------------

        note_label = tk.Label(
            self.window,
            text="Note",
            bg=self.theme["content"],
            fg=self.theme["text"]
        )

        note_label.pack()

        self.note_entry = tk.Entry(
            self.window
        )

        self.note_entry.pack(pady=5)

        self.note_entry.insert(
            0,
            self.expense_data["note"]
        )

        # ---------------------------
        # Buttons
        # ---------------------------

        button_frame = tk.Frame(
            self.window,
            bg=self.theme["content"]
        )

        button_frame.pack(pady=20)

        # Save button
        save_button = tk.Button(
            button_frame,
            text="Save",
            bg=self.theme["accent"],
            fg=self.theme["text"],
            font=BUTTON_FONT,
            command=self.save_changes
        )

        save_button.pack(
            side="left",
            padx=10
        )

        # Delete button
        delete_button = tk.Button(
            button_frame,
            text="Delete",
            bg=self.theme["danger"],
            fg=self.theme["text"],
            font=BUTTON_FONT,
            command=self.delete_expense_data
        )

        delete_button.pack(
            side="left",
            padx=10
        )

    # -------------------------------------------------

    def save_changes(self):

        success, result = edit_expense(
            self.expense_data["id"],
            self.amount_entry.get(),
            self.category_dropdown.cget("text"),
            self.note_entry.get()
        )

        if success:

            Toast(self.parent, "💹 Expense updated successfully.")

            self.refresh_callback()

            self.window.destroy()

        else:

            Toast(self.parent, "❌ Failed to update expense.")

    # -------------------------------------------------

    def delete_expense_data(self):

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this expense?"
        )

        if not confirm:
            return

        success, result = delete_expense(
            self.expense_data["id"]
        )

        if success:

            Toast(self.parent, "🗑 Expense deleted successfully.")

            self.refresh_callback()

            self.window.destroy()

        else:

            Toast(self.parent, "❌ Failed to delete expense.")