#Random Password Generator
#Author -  Chethana K

import tkinter as tk
from tkinter import StringVar
import random
import string
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_generate():
    password_length = int(entry.get())
    generated_password = generate_password(password_length)
    password_text.delete("1.0", tk.END)
    password_text.insert(tk.END, generated_password)

def on_copy():
    password_to_copy = password_text.get("1.0", tk.END).strip()
    pyperclip.copy(password_to_copy)

# Create the main window
window = tk.Tk()
window.title("Random Password Generator")

# Create and place the widgets
entry_label = tk.Label(window, text="Enter Password Length:")
entry_label.pack(padx=10, pady=5)

entry = tk.Entry(window)
entry.pack(padx=10, pady=5)
entry.insert(0, "12")  # default value

generate_button = tk.Button(window, text="Generate", command=on_generate)
generate_button.pack(padx=10, pady=20)

password_text = tk.Text(window, height=2, width=30)
password_text.pack(padx=10, pady=5)

copy_button = tk.Button(window, text="Copy", command=on_copy)
copy_button.pack(padx=10, pady=20)

# Start the Tkinter event loop
window.mainloop()
