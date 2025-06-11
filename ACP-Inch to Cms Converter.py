import tkinter as tk

def convert_to_cm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except ValueError:
        result_label.config(text="Enter a valid number")

# Set up window
root = tk.Tk()
root.title("Inch to CM Converter")
root.geometry("300x150")

# Input field
entry_label = tk.Label(root, text="Enter inches:")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start GUI
root.mainloop()
