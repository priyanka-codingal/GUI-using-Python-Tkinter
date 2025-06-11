import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Enter a positive number")
            return
        
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        result_label.config(text=password)
    except ValueError:
        result_label.config(text="Enter a valid number")

# Set up window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x200")

# Length Entry
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", wraplength=300, fg="blue")
result_label.pack(pady=10)

# Start GUI
root.mainloop()
