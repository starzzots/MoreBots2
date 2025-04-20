import tkinter as tk

class TransparentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transparent App")
        self.root.geometry("720x480")
        self.root.attributes("-alpha", 0.5)  # 50% opacity
        self.root.overrideredirect(True)  # Frameless
        self.root.configure(bg="black")  # Black background

        # Enable window dragging
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.on_move)

        # Create home screen with scalable buttons
        self.create_home_screen()

    def clear_screen(self):
        """Remove all widgets from the window before switching screens."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_home_screen(self):
        """Create the dynamic home screen with multiple buttons."""
        self.clear_screen()

        # Buttons to display on the home screen (Scalable)
        buttons = {
            "Make Script": lambda: self.open_new_screen("Make Script"),
            "Run Script": lambda: self.open_new_screen("Run Script"),
            "Stop Script": lambda: self.open_new_screen("Stop Script")
        }

        # Create buttons dynamically
        for idx, (text, command) in enumerate(buttons.items()):
            btn = tk.Label(self.root, text=text, fg="white", bg="black",
                           font=("Arial", 14, "bold"), cursor="hand2")
            btn.pack(pady=10)
            btn.bind("<Button-1>", lambda event, cmd=command: cmd())

        # Exit button (top-right)
        self.exit_button = tk.Button(self.root, text="X", command=self.root.quit, bg="red",
                                     fg="white", font=("Arial", 12, "bold"), bd=0, relief=tk.FLAT)
        self.exit_button.place(x=690, y=10, width=20, height=20)

    def open_new_screen(self, screen_name):
        """Switch to a new screen based on button clicked."""
        self.clear_screen()

        # Title for the new screen
        new_label = tk.Label(self.root, text=f"{screen_name} Screen", fg="white", bg="black",
                             font=("Arial", 20, "bold"))
        new_label.pack(pady=50)

        # Back button
        back_button = tk.Button(self.root, text="Back", command=self.create_home_screen,
                                bg="gray", fg="white", font=("Arial", 12, "bold"), bd=0, relief=tk.FLAT)
        back_button.pack(pady=20)

    def start_move(self, event):
        """Store the initial click position."""
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        """Move the window."""
        self.root.geometry(f"+{event.x_root - self.x}+{event.y_root - self.y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TransparentApp(root)
    root.mainloop()
