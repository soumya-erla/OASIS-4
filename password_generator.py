import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    length = length_var.get()
    
    if length <= 0:
        messagebox.showerror("Error", "Length must be greater than 0")
        return
    
    characters = ""
    
    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation
    
    if characters == "":
        messagebox.showerror("Error", "Select at least one option!")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.config(bg="#1e1e2f")

# Title
title = tk.Label(root, text="🔐 Password Generator", font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

# Length input
length_var = tk.IntVar(value=12)
tk.Label(root, text="Password Length:", bg="#1e1e2f", fg="white").pack()
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack(pady=5)

# Options
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var, bg="#1e1e2f", fg="white", selectcolor="#2e2e3e").pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, bg="#1e1e2f", fg="white", selectcolor="#2e2e3e").pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="#1e1e2f", fg="white", selectcolor="#2e2e3e").pack()

# Generate button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white")
generate_btn.pack(pady=10)

# Password display
password_entry = tk.Entry(root, font=("Arial", 12), justify="center")
password_entry.pack(pady=10)

# Copy button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_password, bg="#2196F3", fg="white")
copy_btn.pack(pady=5)

# Run app
root.mainloop()