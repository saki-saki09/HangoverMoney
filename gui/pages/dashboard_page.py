import tkinter as tk
from tkinter import ttk 

from utils.storage import load_data

from modules.filter_expense import (
    filter_expenses
)

from gui.styles import (
    NORMAL_FONT,
    get_theme,
    TITLE_FONT,
    BOLD_FONT
)

from gui.components.expense_table import (
    ExpenseTable
)

from gui.components.summary_cards import SummaryCards

from modules.summary import (
    get_total_expenses
)

from gui.components.summary_cards import (
    SummaryCards
)


class DashboardPage:

    def __init__(self, parent):

        self.theme = get_theme()

        self.frame = tk.Frame(parent)

        # Scroll Canvas
        self.canvas = tk.Canvas(
            self.frame,
            bg = self.theme["content"],
            highlightthickness=0
        )

        # Mousewheel support
        self.canvas.bind_all(
            "<MouseWheel>",
            self._on_mousewheel
        )

        # Vertical Scrollbar
        self.scrollbar = tk.Scrollbar(
            self.frame,
            orient = "vertical",
            command=self.canvas.yview
        )

        # Scrollable content frame
        self.content_frame = tk.Frame(
            self.canvas,
            bg = self.theme["content"]
        )

        # Update scroll region
        self.content_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        # Add content frame to canvas
        self.canvas.create_window(
            (0, 0),
            window = self.content_frame,
            anchor="nw"
        )

        # connect scroll bar
        self.canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        # Pack Everything
        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.scrollbar.pack(
            side="right",
            fill="y"
        )


        self.setup_ui()

        self.refresh_data()

    
    # -------------------------------------------------
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )

    # -------------------------------------------------

    def setup_ui(self):

        title = tk.Label(
            self.content_frame,
            text="Dashboard",
            bg=self.theme["content"],
            fg= self.theme["text"],
            font=TITLE_FONT
        )

        title.pack(
            anchor="nw",
            padx=20,
            pady=20
        )

        subtitle = tk.Label(
            self.content_frame,
            text="Welcome to HANGOVER MONEY, where money keeps hanging over your head!",
            bg=self.theme["content"],
            fg= "#FFD700",
            font= BOLD_FONT
        )

        subtitle.pack(
            anchor="nw",
            padx=20,
            pady=10
        )

        # -------------------------------------------------
        # SEARCH SECTION
        # -------------------------------------------------

        search_frame = tk.Frame(
            self.content_frame,
            bg=self.theme["content"]
        )

        search_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Search box
        self.search_keyword = tk.Label(
            search_frame,
            text = "Search Keyword",
            font=TITLE_FONT,
            fg=self.theme["text"],
            bg=self.theme["content"]
        )
        self.search_keyword.pack(
            side="left",
            padx=5
        )
        self.search_entry = tk.Entry(
            search_frame,
            font=NORMAL_FONT,
            width=30
        )

        self.search_entry.pack(
            side="left",
            padx=5
        )

        # Category dropdown
        self.search_category = tk.Label(
            search_frame,
            text="Category",
            font=TITLE_FONT,
            fg=self.theme["text"],
            bg=self.theme["content"]
        )
        self.search_category.pack(
            side="left",
            padx=5
        )
        self.category_var = tk.StringVar()

        self.category_var.set("All")

        categories = [
            "All",
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

        category_dropdown = ttk.Combobox(
            search_frame,
            textvariable=self.category_var,
            values=categories,
            state="readonly",
            width=20
        )

        category_dropdown.pack(
            side="left",
            padx=5
        )

        # Search button
        search_button = tk.Button(
            search_frame,
            text="Search",
            bg=self.theme["button"],
            fg=self.theme["text"],
            command=self.apply_filters
        )

        search_button.pack(
            side="left",
            padx=5
        )

        # Reset button
        reset_button = tk.Button(
            search_frame,
            text="Reset",
            bg=self.theme["button"],
            fg=self.theme["text"],
            command=self.reset_filters
        )

        reset_button.pack(
            side="left",
            padx=5
        )

        # -------------------------------------------------
        # SUMMARY SECTION
        # -------------------------------------------------

        self.summary_frame = tk.Frame(
            self.content_frame,
            bg=self.theme["content"]
        )

        self.summary_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Total expense
        success, total = (
            get_total_expenses()
        )

        if not success:
            total = 0

        self.summary_cards = SummaryCards(
            self.summary_frame,
            self.theme
        )

        self.summary_cards.frame.pack(
            side="left",
            padx=10,
            pady=10
        )

        # Expense table
        self.expense_table = ExpenseTable(
            self.content_frame,
            self.refresh_data
        )

        self.expense_table.frame.pack(
            fill="both",
            expand=True
        )

        # -------------------------------------------------
        # CHART SECTION
        # -------------------------------------------------

        self.chart_container = tk.Frame(
            self.content_frame,
            bg=self.theme["content"]
        )

        self.chart_container.pack(
            pady=10
        )
    
    
    def apply_filters(self):

        search_text = (
            self.search_entry.get()
        )

        category = (
            self.category_var.get()
        )

        filtered_data = filter_expenses(
            search_text=search_text,
            category=category
        )

        self.expense_table.load_custom_data(
            filtered_data
        )


    # -------------------------------------------------

    def reset_filters(self):

        self.search_entry.delete(0, tk.END)

        self.category_var.set("All")

        self.expense_table.refresh()
    
    def refresh_theme(self):

        self.theme = get_theme()

        self.content_frame.configure(
            bg=self.theme["content"]
    )
    
    def refresh_data(self):

        # Refresh summary cards
        self.refresh_summary_cards()

        # Refresh expense table
        self.refresh_table()

        # Refresh charts
        self.refresh_chart()
    
    def refresh_summary_cards(self):
        self.summary_cards.refresh()
    
    def refresh_table(self):

        search_text = (
            self.search_entry.get()
        )

        category = (
            self.category_var.get()
        )

        filtered_data = filter_expenses(
            search_text=search_text,
            category=category
        )

        self.expense_table.load_custom_data(
            filtered_data
        )
    
    def refresh_chart(self):

        # Clear old charts
        for widget in (
            self.chart_container.winfo_children()
        ):
            widget.destroy()

        from gui.components.chart_view import (
            ChartView
        )

        chart = ChartView(
            self.chart_container,
            self.theme
        )

        chart.frame.pack(fill="both", expand=True)
        chart.refresh()