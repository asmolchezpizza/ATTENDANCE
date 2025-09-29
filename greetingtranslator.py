import tkinter as tk
from tkinter import ttk

class TranslatorApp:
    """
    A Tkinter application to translate a welcome greeting using a class-based structure.
    The main greeting is placed below the language selection buttons.
    """
    def __init__(self, master):
        # 1. Setup the main window properties
        self.master = master
        master.title("Multilingual Greeting Selector")
        master.geometry("550x250")
        master.resizable(False, False)
        
        # Define the translations
        self.greetings = {
            "English": "Welcome! Hello!",
            "Spanish": "¡Bienvenido! ¡Hola!",
            "French": "Bienvenue! Bonjour!",
            "Dutch": "Welkom! Hallo!"
        }
        
        # Set up a modern theme and configure columns for centering
        style = ttk.Style()
        style.theme_use('alt')
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

        # 2. Widgets placed according to the new layout
        
        # A. Instruction Label (Row 0 - Top Message)
        self.instruction_label = ttk.Label(
            master, 
            text="Please select one of the languages below:", 
            font=("Inter", 12),
            padding=(0, 15, 0, 10)
        )
        # Span across all 4 columns, sticky "n" anchors it to the top
        self.instruction_label.grid(row=0, column=0, columnspan=4, sticky="n")

        # B. Language Buttons (Row 1)
        languages = ["English", "Spanish", "French", "Dutch"]
        
        for i, lang in enumerate(languages):
            # Create button with a command that calls update_greeting with the language key
            button = ttk.Button(
                master,
                text=lang,
                command=lambda l=lang: self.update_greeting(l)
            )
            
            # Place button in Row 1, Columns 0 through 3. 'ew' makes it fill the width.
            button.grid(row=1, column=i, padx=10, pady=10, sticky="ew")

        # C. Main Greeting Label (Row 2 - Output, Placed Below Buttons)
        self.main_greeting = ttk.Label(
            master, 
            text=self.greetings["English"],  # Initial greeting
            font=("Inter", 26, "bold"),
            foreground="#1B4F72", # A nice deep blue color
            padding=(20, 20, 20, 10)
        )
        # Span across all 4 columns for a clean look
        self.main_greeting.grid(row=2, column=0, columnspan=4, sticky="n", pady=(10, 0))

    def update_greeting(self, language_key):
        """
        Updates the text of the main greeting label based on the selected language.
        """
        new_greeting = self.greetings.get(language_key, "Error: Language not found.")
        self.main_greeting.config(text=new_greeting)

# Main execution block
if __name__ == '__main__':
    # Create the root window
    root = tk.Tk()
    
    # Create and run the application instance
    app = TranslatorApp(root)
    
    # Start the event loop
    root.mainloop()