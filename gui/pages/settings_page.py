import tkinter as tk

from gui.styles import *

from utils.config import (
    get_setting,
    set_setting
)

from modules.export_data import (
    export_to_json,
    export_to_csv,
    export_to_excel,
    export_to_pdf,
    open_export_folder
)

from gui.components.toast import Toast

from utils.helpers import resource_path


class SettingsPage:

    def __init__(self, parent, dashboard):

        self.parent = parent
        self.theme = get_theme()

        self.frame = tk.Frame(
            parent,
            bg=self.theme["content"]
        )
        
        self.dashboard = dashboard

        self.setup_ui()

    # -------------------------------------------------

    def setup_ui(self):

        title = tk.Label(
            self.frame,
            text="Settings",
            bg=self.theme["content"],
            fg=self.theme["text"],
            font=TITLE_FONT
        )

        title.pack(pady=20)

        # Theme label
        theme_label = tk.Label(
            self.frame,
            text="Theme:",
            bg=self.theme["content"],
            fg=self.theme["text"],
            font=NORMAL_FONT
        )

        theme_label.pack()

        # Theme dropdown
        self.theme_var = tk.StringVar()

        self.theme_var.set(
            get_setting("theme")
        )

        dropdown = tk.OptionMenu(
            self.frame,
            self.theme_var,
            "dark",
            "light"
        )

        dropdown.pack(pady=10)

        # Save button
        save_button = tk.Button(
            self.frame,
            text="Save Settings",
            bg=self.theme["accent"],
            fg=self.theme["text"],
            font=BUTTON_FONT,
            command=self.save_settings
        )

        save_button.pack(pady=20)

        # Export Sections
        export_frame = tk.LabelFrame(
            self.frame,
            text = "Export System",
            bg = self.theme["content"],
            fg = self.theme["text"],
            font = BOLD_FONT,
            padx = 20,
            pady = 20
        )

        export_frame.pack(
            fill = "x",
            padx = 20,
            pady = 20
        )

        json_button = tk.Button(
            export_frame,
            text = "Export JSON",
            command = self.export_json,
            bg = self.theme["button"],
            fg = "#ffffff",
            width = 20
        )

        json_button.grid(
            row = 0,
            column = 0,
            padx = 10,
            pady = 10
        )

        csv_button = tk.Button(
            export_frame,
            text = "Export CSV",
            command = self.export_csv,
            bg = self.theme["button"],
            fg = "#ffffff",
            width = 20
        )

        csv_button.grid(
            row = 0,
            column = 1,
            padx = 10,
            pady = 10
        )

        excel_button = tk.Button(
            export_frame,
            text = "Export Excel",
            command = self.export_excel,
            bg = self.theme["button"],
            fg = "#ffffff",
            width = 20
        )

        excel_button.grid(
            row = 0,
            column = 2,
            padx = 10,
            pady = 10
        )

        pdf_button = tk.Button(
            export_frame,
            text = "Export PDF",
            command = self.export_pdf,
            bg = self.theme["button"],
            fg = "#ffffff",
            width = 20
        )

        pdf_button.grid(
            row = 0,
            column = 3,
            padx = 10,
            pady = 10
        )

        open_folder_button = tk.Button(
            export_frame,
            text = "Open Export Folder",
            command = self.export_folder,
            bg = self.theme["button"],
            fg = "#ffffff",
            width = 20
        )

        open_folder_button.grid(
            row = 1,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 10
        )


    # -------------------------------------------------

    def save_settings(self):

        set_setting(
            "theme",
            self.theme_var.get()
        )

        # Refresh entire GUI
        self.dashboard.refresh_theme()

    # -------------------------------------------------

    def export_json(self):

        success, message = export_to_json()

        if success:
            Toast(
                self.frame,
                "JSON Export Successful",
                "#2ecc71"
            )

        else:
            Toast(
                self.frame,
                message,
                "#e74c3c"
            )


    def export_csv(self):

        success, message = export_to_csv()

        if success:
            Toast(
                self.frame,
                "CSV Export Successful",
                "#2ecc71"
            )

        else:
            Toast(
                self.frame,
                message,
                "#e74c3c"
            )


    def export_excel(self):

        success, message = export_to_excel()

        if success:
            Toast(
                self.frame,
                "Excel Export Successful",
                "#2ecc71"
            )

        else:
            Toast(
                self.frame,
                message,
                "#e74c3c"
            )


    def export_pdf(self):

        success, message = export_to_pdf()

        if success:
            Toast(
                self.frame,
                "PDF Export Successful",
                "#2ecc71"
            )

        else:
            Toast(
                self.frame,
                message,
                "#e74c3c"
            )
    
    def export_folder(self):
        open_export_folder()