import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

def submit_feedback():
    """
    Function to handle the submission.
    It retrieves the text from all widgets and prints it to the console.
    """
    # 1. Retrieve data from all fields
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    feedback_text = feedback_area.get('1.0', tk.END).strip()

    # 2. Basic Validation: Ensure feedback text is not empty
    if not feedback_text:
        messagebox.showerror("Error", "Please enter your feedback before submitting.")
        return

    # 3. Print the data to the console
    print("--- Feedback Submission Details ---")
    print(f"Name: {name if name else 'N/A'}")
    print(f"Email: {email if email else 'N/A'}")
    print("-----------------------------------")
    print(f"Feedback:")
    print(feedback_text)
    print("-----------------------------------")

    # 4. Clear the text areas and show confirmation
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_area.delete('1.0', tk.END)
    messagebox.showinfo("Success", "Thank you for your feedback! It has been submitted.")


# 1. Initialize the main window
app = tk.Tk()
app.title("Customer Feedback Form")
app.geometry("550x450")
app.columnconfigure(1, weight=1) # Allows the input column to expand

# --- Main Instructions ---
# Message at the top asking the user to submit feedback
instruction_label = tk.Label(
    app,
    text="Please submit your valuable feedback below.",
    font=("Arial", 14, "bold")
)
# Use grid for structured layout
instruction_label.grid(row=0, column=0, columnspan=2, pady=15, padx=10, sticky="ew")

# --- Name Input ---
tk.Label(app, text="Name (Optional):", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(app, width=50, font=("Arial", 10))
name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# --- Email Input ---
tk.Label(app, text="Email (Optional):", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(app, width=50, font=("Arial", 10))
email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# --- Feedback Label ---
tk.Label(app, text="Your Experience Feedback:", font=("Arial", 10, "bold")).grid(row=3, column=0, columnspan=2, padx=10, pady=(15, 5), sticky="w")

# --- Feedback Text Area ---
# Using scrolledtext for automatic scrolling
feedback_area = scrolledtext.ScrolledText(
    app,
    wrap=tk.WORD,
    width=50,
    height=10,
    font=("Arial", 10)
)
# The text area spans both columns and expands vertically and horizontally
feedback_area.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
app.rowconfigure(4, weight=1) # Allows this row to expand when the window is resized

# --- Submit Button ---
submit_button = tk.Button(
    app,
    text="Submit Feedback",
    command=submit_feedback,
    font=("Arial", 12, "bold")
)
submit_button.grid(row=5, column=0, columnspan=2, pady=20)

# 5. Start the Tkinter event loop
app.mainloop()