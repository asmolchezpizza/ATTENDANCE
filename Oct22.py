import tkinter as tk
from tkinter import messagebox, scrolledtext
from openai import OpenAI
import threading
import TommysAPIKey
apikey = TommysAPIKey.OPEN_AI_KEY

# --- Functions ---

def get_openai_answer(question):
    """
    This function runs in a separate thread to call the OpenAI API.
    """
    try:
        # 1. Initialize the client
        # This automatically looks for the OPENAI_API_KEY environment variable
        client = OpenAI(
            api_key=apikey
        )

        # 2. Make the API call
        # I've updated this to the correct, modern API call structure.
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using a valid, current model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        
        # 3. Extract the answer
        answer = response.choices[0].message.content

    except Exception as e:
        # Handle API errors (e.g., no API key, network issues)
        answer = f"Error: Could not retrieve answer.\n{e}"

    # 4. Safely schedule the GUI update on the main thread
    # We cannot update tkinter widgets from a background thread directly.
    # root.after(0, ...) tells the main thread to run this function ASAP.
    root.after(0, update_answer_box, answer)

def update_answer_box(answer):
    """
    This function safely updates the answer box from the main thread.
    """
    # Set the state to 'normal' so we can write to it
    text_answer.config(state='normal')
    
    # Clear any previous content
    text_answer.delete("1.0", tk.END)
    
    # Insert the new answer
    text_answer.insert(tk.END, answer)
    
    # Set the state back to 'disabled' so the user can't type in it
    text_answer.config(state='disabled')

def process_question():
    """
    This function is called when the submit button is pressed.
    It starts the background thread to get the answer.
    """
    # 1. Get the text from the question entry box
    question = entry_question.get()

    if not question:
        messagebox.showwarning("Empty Field", "Please ask a question first.")
        return

    # 2. Clear the question box
    entry_question.delete(0, tk.END)

    # 3. Show a "Loading..." message in the answer box
    update_answer_box("Loading... Please wait for the AI to respond.")

    # 4. Start the API call in a new thread to avoid freezing the GUI
    # We pass the 'question' as an argument to the target function
    thread = threading.Thread(target=get_openai_answer, args=(question,))
    thread.start()

# --- Set up the main window ---
root = tk.Tk()
root.title("Question and Answer (with OpenAI)")
root.geometry("500x450") # Made window larger

# --- Create the GUI widgets ---

# 1. Label for the question box
label_question = tk.Label(root, text="Ask your question:", font=("Arial", 12))

# 2. The Entry box (for typing the question)
entry_question = tk.Entry(root, width=60, font=("Arial", 11))

# 3. The Submit button
button_submit = tk.Button(root, text="Submit", font=("Arial", 11, "bold"), command=process_question)

# 4. Label for the answer box
label_answer = tk.Label(root, text="Answer:", font=("Arial", 12))

# 5. The Output box (Changed to ScrolledText for long answers)
text_answer = scrolledtext.ScrolledText(root, height=15, width=60, font=("Arial", 11), wrap=tk.WORD)
text_answer.config(state='disabled') # Start in 'disabled' mode

# --- Place the widgets in the window ---
label_question.pack(pady=(10, 5))
entry_question.pack(pady=5, padx=20)
button_submit.pack(pady=10)
label_answer.pack(pady=5)
text_answer.pack(pady=5, padx=20, fill="both", expand=True)

# --- Start the application ---
root.mainloop()