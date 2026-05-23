from utils.config import get_setting


# -------------------------------------------------
# THEMES
# -------------------------------------------------

DARK_THEME = {
    "background": "#1e1e1e",
    "sidebar": "#252526",
    "content": "#2d2d30",
    "text": "#ffffff",
    "button": "#3a3d41",
    "accent": "#4cc2ff",
    "danger": "#ff4d4d",
    "card": "#3a3d41"
}


LIGHT_THEME = {
    "background": "#f5f5f5",
    "sidebar": "#dddddd",
    "content": "#ffffff",
    "text": "#000000",
    "button": "#cccccc",
    "accent": "#0078d7",
    "danger": "#ff4d4d",
    "card": "#ffffff"
}


# -------------------------------------------------
# GET CURRENT THEME
# -------------------------------------------------

def get_theme():

    current_theme = get_setting("theme")

    if current_theme == "light":
        return LIGHT_THEME

    return DARK_THEME


# -------------------------------------------------
# FONTS
# -------------------------------------------------

TITLE_FONT = ("Segoe UI", 20, "bold")

NORMAL_FONT = ("Segoe UI", 11)

BOLD_FONT = ("Segoe UI", 11, "bold")

BUTTON_FONT = ("Segoe UI", 10, "bold")