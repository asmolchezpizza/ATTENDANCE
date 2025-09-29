import tkinter as tk
from tkinter import Text, Entry, Label, Button

def submit_feedback():
    """
    Retrieves the text from the input fields and prints it to the console.
    """
    name = name_entry.get()
    email = email_entry.get()
    # The "1.0" means get text from the first line, character zero.
    # tk.END means get text until the end.
    feedback = feedback_text.get("1.0", tk.END)

    # Print the collected data to the console with clear labels.
    print("--- Customer Feedback Received ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    # Use .strip() to remove any extra whitespace or newlines from the feedback text.
    print(f"Feedback: {feedback.strip()}")
    print("----------------------------------\n")


# --- Main Application Window Setup ---
# Create the main window (the root)
root = tk.Tk()
root.title("Feedback Form")
# Set a reasonable default size for the window
root.geometry("450x400")

# --- Create and Place Widgets using the .grid() layout manager ---

# 1. Main instruction label at the top
main_label = Label(root, text="Please submit your feedback.", font=("Helvetica", 14))
main_label.grid(row=0, column=0, columnspan=2, pady=15, padx=10)

# 2. Name input label and entry box
name_label = Label(root, text="Name:")
# 'sticky="w"' aligns the label to the west (left) side of its grid cell.
name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
name_entry = Entry(root, width=50)
name_entry.grid(row=1, column=1, padx=10, pady=5)

# 3. Email input label and entry box
email_label = Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
email_entry = Entry(root, width=50)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# 4. Feedback input label and text box
feedback_label = Label(root, text="Feedback:")
# 'sticky="nw"' aligns the label to the north-west (top-left) corner.
feedback_label.grid(row=3, column=0, padx=10, pady=5, sticky="nw")
feedback_text = Text(root, height=10, width=37)
feedback_text.grid(row=3, column=1, padx=10, pady=5)

# 5. Submit Button
# The 'command' parameter is set to the function that should be executed on click.
submit_button = Button(root, text="Submit", command=submit_feedback)
# 'sticky="e"' aligns the button to the east (right) side of its grid cell.
submit_button.grid(row=4, column=1, pady=20, padx=10, sticky="e")

# --- Start the GUI event loop ---
# This line keeps the window open and responsive to user actions.
root.mainloop()