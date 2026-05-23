import tkinter as tk

class Toast:
    def __init__(self, parent, message, bg = "#333333"):
        self.window = tk.Toplevel(parent)
        self.window.overrideredirect(True)
        self.window.configure(bg=bg)

        # position top right of the screen...
        self.window.geometry("300x60+1200+80")

        label = tk.Label(
            self.window,
            text = message,
            font =("Segoe UI", 12, "bold"),
            fg = "#ffffff",
            bg=bg
        )

        label.pack(
            expand=True,
            fill="both",
            padx=10,
            pady=10
        )

        # auto close after 2 seconds
        self.window.after(2000, self.window.destroy)
        