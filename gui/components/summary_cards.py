import tkinter as tk
from utils.storage import load_data

class SummaryCards:

    def __init__(self, parent, theme):
        self.parent = parent
        self.theme = theme

        # Main frame for all cards
        self.frame = tk.Frame(parent, bg=self.theme["background"])
        self.frame.pack(fill="x", padx=20, pady=10)

        self.load_cards()

    # Create a single card
    def create_card(self, title, value):
        card = tk.Frame(self.frame, bg=self.theme["card"], width=220, height=100)
        card.pack(side="left", padx=10)
        card.pack_propagate(False)

        title_label = tk.Label(card, text=title, font=("Segoe UI", 12), fg="gray", bg=self.theme["card"])
        title_label.pack(pady=(15, 5))

        value_label = tk.Label(card, text=value, font=("Segoe UI", 20, "bold"), fg="white", bg=self.theme["card"])
        value_label.pack()

    # Load all cards dynamically
    def load_cards(self):
        expenses = load_data()

        total_expense = sum(expense["amount"] for expense in expenses)
        total_categories = len(set(expense["category"] for expense in expenses))
        highest_expense = max([expense["amount"] for expense in expenses], default=0)

        self.create_card("Total Expenses", f"৳{total_expense}")
        self.create_card("Categories", str(total_categories))
        self.create_card("Highest Expense", f"৳{highest_expense}")

    # Refresh cards when data changes
    def refresh(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.load_cards()