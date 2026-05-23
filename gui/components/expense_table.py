from operator import index
import tkinter as tk

from tkinter import ttk

from gui.styles import *
from gui.components.toast import Toast
from modules.edit_expense import (
    edit_expense
)
from modules.delete_expense import (
    delete_expense
)
from modules.view_expense import (
    get_all_expenses
)

from gui.components.edit_popup import (
    EditPopup
)

from modules.view_expense import (
    get_expense_by_id
)


class ExpenseTable:

    def __init__(
        self,
        parent,
        refresh_callback=None
    ):

        self.parent = parent
        self.parent_refresh = refresh_callback
        self.theme = get_theme()

        self.frame = tk.Frame(
            parent,
            bg=self.theme["content"]    
        )

        self.setup_table()

        self.load_data()

    # -------------------------------------------------

    def setup_table(self):

        # Context menu
        self.menu = tk.Menu(
            self.frame,
            tearoff=0
        )

        self.menu.add_command(
            label="Edit",
            command=self.edit_selected
        )

        self.menu.add_command(
            label="Delete",
            command=self.delete_selected
        )

        columns = (
            "Amount",
            "Category",
            "Note",
            "Date-TIME"
        )

        self.tree = ttk.Treeview(
            self.frame,
            columns=columns,
            show="headings",
            height=15
        )
        
        # Right click binding
        self.tree.bind(
            "<Button-3>",
            self.show_context_menu
        )

        # Headings
        for column in columns:

            self.tree.heading(
                column,
                text=column,
                command=lambda c=column:
                self.sort_column(c, False)
            )

            self.tree.column(
                column,
                width=150
            )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # Double click event
        self.tree.bind(
            "<Double-1>",
            self.open_edit_popup
        )
    
        # Delete key
        self.tree.bind(
            "<Delete>",
            lambda event:
            self.delete_selected()
        )

        # Enter key
        self.tree.bind(
            "<Return>",
            lambda event:
            self.edit_selected()
        )

        # Refresh key
        self.tree.bind(
            "<F5>",
            lambda event:
            self.refresh()
        )

    # -------------------------------------------------
    def show_context_menu(self, event):

        selected = self.tree.identify_row(
            event.y
        )

        if selected:

            self.tree.selection_set(selected)

            self.menu.post(
                event.x_root,
                event.y_root
            )


    # -------------------------------------------------

    def edit_selected(self):

        selected_item = self.tree.selection()

        if not selected_item:
            return

        expense_id = selected_item[0]

        success, expense_data = (
            get_expense_by_id(expense_id)
        )

        if not success:
            return

        EditPopup(
            self.frame,
            expense_data,
            self.parent_refresh
        )


    # -------------------------------------------------

    def delete_selected(self):

        selected_item = self.tree.selection()

        if not selected_item:
            return

        expense_id = selected_item[0]

        success, result = delete_expense(
            expense_id
        )

        if success:

            Toast(self.parent, "🗑 Expense deleted successfully.")

            # FULL dashboard refresh
            if self.parent_refresh:

                self.parent_refresh()
    
    def load_data(self):

        # Clear existing rows
        for row in self.tree.get_children():

            self.tree.delete(row)

        success, expenses = (
            get_all_expenses()
        )

        if not success:
            return

        # Empty state
        if not expenses:

            self.tree.insert(
                "",
                "end",
                values=(
                    "No Data",
                    "",
                    "",
                    ""
                )
            )

            return

        # Insert expenses
        for index, expense in enumerate(expenses):

            tag = (
                "evenrow"
                if (index % 2) == 0
                else "oddrow"
            )

            self.tree.insert(
                "",
                "end",
                iid=expense["id"],
                values=(
                    expense["amount"],
                    expense["category"],
                    expense["note"],
                    expense["date"]
                ),
                tags=(tag,)
            )
    # -------------------------------------------------

    def load_custom_data(self, data):

        # Clear existing rows
        for row in self.tree.get_children():

            self.tree.delete(row)

        # Insert filtered rows
        for expense in data:

            self.tree.insert(
                "",
                "end",
                iid=expense["id"],
                values=(
                    expense["amount"],
                    expense["category"],
                    expense["note"],
                    expense["date"]
                )
            )

    # -------------------------------------------------

    def open_edit_popup(self, event):

        selected_item = self.tree.selection()

        if not selected_item:
            return

        expense_id = selected_item[0]

        success, expense_data = (
            get_expense_by_id(expense_id)
        )

        if not success:
            return

        EditPopup(
            self.frame,
            expense_data,
            self.parent_refresh
        )
    
    def sort_column(self, column, reverse):

        data = []

        for item in self.tree.get_children():

            value = self.tree.set(item, column)

            data.append((value, item))

        # Numeric sorting for Amount
        if column == "Amount":

            data.sort(
                key=lambda x: float(x[0]),
                reverse=reverse
            )

        else:

            data.sort(
                reverse=reverse
            )

        # Rearrange rows
        for index, (_, item) in enumerate(data):

            self.tree.move(
                item,
                "",
                index
            )

        # Reverse next click
        self.tree.heading(
            column,
            command=lambda:
            self.sort_column(
                column,
                not reverse
            )
        )
    
    def refresh(self):

        self.load_data()
    