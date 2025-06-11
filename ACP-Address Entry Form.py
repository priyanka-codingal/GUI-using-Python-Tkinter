import tkinter as tk

def submit_form():
    name = name_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zipcode = zip_entry.get()

    print("Submitted Information:")
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"City: {city}")
    print(f"State: {state}")
    print(f"Zip Code: {zipcode}")

    # Optional: clear the form
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    state_entry.delete(0, tk.END)
    zip_entry.delete(0, tk.END)

# Set up main window
root = tk.Tk()
root.title("Address Entry Form")
root.geometry("350x300")

# Labels and Entry fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10)

tk.Label(root, text="Address").grid(row=1, column=0, padx=10, pady=5, sticky="w")
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=1, column=1, padx=10)

tk.Label(root, text="City").grid(row=2, column=0, padx=10, pady=5, sticky="w")
city_entry = tk.Entry(root, width=30)
city_entry.grid(row=2, column=1, padx=10)

tk.Label(root, text="State").grid(row=3, column=0, padx=10, pady=5, sticky="w")
state_entry = tk.Entry(root, width=30)
state_entry.grid(row=3, column=1, padx=10)

tk.Label(root, text="Zip Code").grid(row=4, column=0, padx=10, pady=5, sticky="w")
zip_entry = tk.Entry(root, width=30)
zip_entry.grid(row=4, column=1, padx=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=1, pady=20)

# Start the GUI loop
root.mainloop()
