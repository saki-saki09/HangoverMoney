import tkinter as tk
from gui.styles import *
from PIL import Image, ImageTk

class Sidebar:
    def __init__(self, parent, page_callback):

        self.theme = get_theme()
        self.frame = tk.Frame(
            parent,
            bg = self.theme["sidebar"],
            width = 252
        )
        self.page_callback = page_callback

        self.setup_sidebar()
    
    # -----------------------------------------

    def setup_sidebar(self):

        # Main product logo
        logo = Image.open("assets/logo.png")
        logo = logo.resize((100, 100), Image.LANCZOS)
        logo = ImageTk.PhotoImage(logo)

        logo_label = tk.Label(
            self.frame,
            image=logo,
            bg=self.theme["sidebar"]
        )
        logo_label.image = logo  # Keep a reference to the image
        logo_label.pack()

        title = tk.Label(
            self.frame,
            text = "Hangover Money",
            bg = self.theme["sidebar"],
            fg = "#FFD700",
            font= TITLE_FONT
        )

        title.pack(pady=30)

        buttons = [
            ("Dashboard", "dashboard"),
            ("Add Expense", "add_expense"),
            ("Settings", "settings")
        ]

        for text, page in buttons:
            button = tk.Button(
                self.frame,
                text = text,
                bg = self.theme["button"],
                fg = self.theme["text"],
                font=BUTTON_FONT,
                relief="flat",
                pady=10,
                cursor="hand2",
                command=lambda p=page:
                self.page_callback(p)
            )
            button.pack(
                fill="x", 
                padx=15, 
                pady=5
            )
