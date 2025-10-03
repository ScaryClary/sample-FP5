import tkinter as tk
from tkinter import ttk

def submit_info():
    """
    Retrieves data from the input fields, prints it, and then clears the fields.
    """
    name = entry_name.get()
    birthday = entry_birthday.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    contact_method = combo_contact.get()
    
    print("--- Customer Information Submitted ---")
    print(f"Name: {name}")
    print(f"Birthday: {birthday}")
    print(f"Email: {email}")
    print(f"Phone Number: {phone}")
    print(f"Address: {address}")
    print(f"Preferred Contact Method: {contact_method}")
    print("------------------------------------")

    # --- NEW: Clear the fields for the next entry ---
    entry_name.delete(0, tk.END)
    entry_birthday.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    combo_contact.set("Email") # Reset combobox to default value


# --- GUI Setup ---
# Create the main window
root = tk.Tk()
root.title("Customer Information Form")
root.geometry("400x300") # Set a default size for the window

# Create a main frame to hold all the widgets
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.pack(fill=tk.BOTH, expand=True)

# --- Create and place widgets ---

# Name
ttk.Label(main_frame, text="Name:").grid(column=0, row=0, sticky=tk.W, pady=5)
entry_name = ttk.Entry(main_frame, width=30)
entry_name.grid(column=1, row=0, sticky=tk.W)

# Birthday
ttk.Label(main_frame, text="Birthday (MM/DD/YYYY):").grid(column=0, row=1, sticky=tk.W, pady=5)
entry_birthday = ttk.Entry(main_frame, width=30)
entry_birthday.grid(column=1, row=1, sticky=tk.W)

# Email
ttk.Label(main_frame, text="Email:").grid(column=0, row=2, sticky=tk.W, pady=5)
entry_email = ttk.Entry(main_frame, width=30)
entry_email.grid(column=1, row=2, sticky=tk.W)

# Phone Number
ttk.Label(main_frame, text="Phone Number:").grid(column=0, row=3, sticky=tk.W, pady=5)
entry_phone = ttk.Entry(main_frame, width=30)
entry_phone.grid(column=1, row=3, sticky=tk.W)

# Address
ttk.Label(main_frame, text="Address:").grid(column=0, row=4, sticky=tk.W, pady=5)
entry_address = ttk.Entry(main_frame, width=30)
entry_address.grid(column=1, row=4, sticky=tk.W)

# Preferred Contact Method Dropdown
ttk.Label(main_frame, text="Preferred Contact:").grid(column=0, row=5, sticky=tk.W, pady=5)
contact_options = ["Email", "Phone", "Text Message"]
combo_contact = ttk.Combobox(main_frame, values=contact_options, width=27)
combo_contact.grid(column=1, row=5, sticky=tk.W)
combo_contact.set("Email") # Set a default value

# Submit Button
submit_button = ttk.Button(main_frame, text="Submit", command=submit_info)
submit_button.grid(column=1, row=6, sticky=tk.E, pady=15)


# Start the GUI event loop
root.mainloop()