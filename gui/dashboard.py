from logging import root
import tkinter as tk

from gui.styles import (
    get_theme
)

from gui.components.sidebar import Sidebar
from gui.components.summary_cards import SummaryCards

from gui.pages.dashboard_page import (
    DashboardPage
)

from gui.pages.add_expense_page import (
    AddExpensePage
)

from gui.pages.settings_page import (
    SettingsPage
)

from utils.helpers import resource_path


class Dashboard:
    def __init__(self):
        # Create main window
        self.root = tk.Tk()
        self.root.iconbitmap(
            resource_path("assets/logo.ico")
        )

        
        self.theme = get_theme()

        #Window settings
        self.root.title("HANGOVER MONEY")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 600)
        self.root.configure(
            bg=self.theme["background"]
        )

        # Store Page
        self.pages = {}

        # Setup layout
        self.setup_layout()
    
    # --------------------------------
    # Main Layout
    # --------------------------------

    def setup_layout(self):

        #Sidebar 
        self.sidebar = Sidebar(
            self.root,
            self.show_page
        )

        self.sidebar.frame.pack(
            side="left",
            fill="y"
        )

        # Content Frame
        self.container = tk.Frame(
            self.root,
            bg=self.theme["content"]
        )

        self.container.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Create pages
        self.create_pages()

        # Default page
        self.show_page("dashboard")
    

    # ------------------------------------------

    def create_pages(self):
        dashboard_page = DashboardPage(
            self.container
        )

        self.pages["dashboard"] = dashboard_page

        self.pages["add_expense"] = (
            AddExpensePage(
                self.container,
                dashboard_page
            )
        )

        self.pages["settings"] = (
            SettingsPage(self.container, self)
        )

    # -------------------------------------------

    def show_page(self, page_name):
        # Hide all pages
        for page in self.pages.values():
            page.frame.pack_forget()
        
        # Show selected page
        self.pages[page_name].frame.pack(
            fill = "both",
            expand = True
        )
    
    # ------------------------------------------

    def refresh_theme(self):

        # Reload theme
        self.theme = get_theme()

        # Update root
        self.root.configure(
            bg=self.theme["background"]
        )

        # Update container
        self.container.configure(
            bg=self.theme["content"]
        )

        # Refresh pages
        for page in self.pages.values():

            if hasattr(page, "refresh_theme"):

                page.refresh_theme()

    # ------------------------------------------

    def run(self):
        self.root.mainloop()