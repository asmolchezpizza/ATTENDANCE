import tkinter as tk
from tkinter import ttk # ttk provides themed widgets

def on_button_click():
    """Function to be executed when the button is pressed."""
    # 1. Get the text from the entry box
    input_text = entry_box.get()

    # 2. Check if the box is empty
    if input_text:
        # 3. Update the output label text
        output_label.config(text=f"Hello, {input_text}!")
    else:
        output_label.config(text="Please enter your name.")

# 1. Create the main window
root = tk.Tk()
root.title("Basic Tkinter App")
# Make the window not resizable to keep layout simple (optional)
root.resizable(False, False)

# 2. Create the widgets

# A. Text Input Box (Entry)
# This is where the user types text.
entry_box = ttk.Entry(root, width=30)
entry_box.grid(row=0, column=0, padx=10, pady=10)

# B. Button
# The command parameter links the button press to the Python function.
action_button = ttk.Button(root, text="Greet Me!", command=on_button_click)
action_button.grid(row=1, column=0, padx=10, pady=10)

# C. Output Display (Label)
# A Label is a simple text area. We will update its text to show output.
output_label = ttk.Label(root, text="Enter your name above and click the button.")
output_label.grid(row=2, column=0, padx=10, pady=10)

# 3. Start the main event loop
# This makes the window appear and waits for user interaction (like button clicks).
root.mainloop()