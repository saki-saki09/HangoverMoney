import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from utils.storage import load_data


class ChartView:

    def __init__(self, parent, theme):

        self.parent = parent
        self.theme = theme

        # MAIN CHART FRAME
        self.frame = tk.Frame(
            parent,
            bg=self.theme["card"]
        )

        self.frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.load_chart()

    def load_chart(self):

        expenses = load_data()

        category_totals = {}

        for expense in expenses:

            category = expense["category"]
            amount = expense["amount"]

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += amount

        labels = list(category_totals.keys())
        amounts = list(category_totals.values())

        # CLEAR OLD CHART
        for widget in self.frame.winfo_children():
            widget.destroy()

        # BIGGER FIGURE
        figure = Figure(
            figsize=(8, 5),
            dpi=100,
            facecolor=self.theme["card"]
        )

        ax = figure.add_subplot(111)

        # DONUT CHART
        wedges, texts, autotexts = ax.pie(
            amounts,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops={
                "width": 0.45
            }
        )

        # TITLE
        ax.set_title(
            "Expense Distribution",
            fontsize=18,
            fontweight="bold",
            color="white",
            pad=20
        )

        # DARK MODE FIX
        ax.set_facecolor(self.theme["card"])

        for text in texts:
            text.set_color("white")
            text.set_fontsize(12)

        for autotext in autotexts:
            autotext.set_color("white")
            autotext.set_fontsize(11)

        # MAKE PERFECT CIRCLE
        ax.axis("equal")

        # TKINTER CANVAS
        canvas = FigureCanvasTkAgg(
            figure,
            master=self.frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    def refresh(self):

        self.load_chart()