import tkinter as tk
from tkinter import messagebox as msgbx

# main window
mw= tk.Tk()
mw.title("CONTACT BOOK")
mw.geometry("400x400")

#to store contacts
contacts = []


# Function to add a new contact
def add_contact():
    name = n.get()
    ph_no =pn.get()
    if name and ph_no:
        contacts.append((name, ph_no))
        update_contacts()
    else:
        msgbx.showwarning("Input Error", "Please enter both name and number")
def update_contacts():
    contact_list.delete(0, tk.END)
    for c in contacts:
        contact_list.insert(tk.END, f"{c[0]}: {c[1]}")


# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        contacts.pop(selected_contact[0])
        update_contacts()
    else:
        msgbx.showwarning("Selection Error", "Please select a contact to delete")


# Function to update a contact
def update_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        name = n.get()
        ph_no = pn.get()
        if name and ph_no:
            contacts[selected_contact[0]] = (name, ph_no)
            update_contacts()
        else:
            msgbx.showwarning("Input Error", "Please enter both name and number")
    else:
        msgbx.showwarning("Selection Error", "Please select a contact to update")

n = tk.StringVar()
pn = tk.StringVar()

tk.Label(mw, text="Contact Name").pack()
tk.Entry(mw, textvariable=n).pack()

tk.Label(mw, text="Contact Number").pack()
tk.Entry(mw, textvariable=pn).pack()

tk.Button(mw, text="Add Contact", command=add_contact).pack()
tk.Button(mw, text="Update Contact", command=update_contact).pack()
tk.Button(mw, text="Delete Contact", command=delete_contact).pack()

contact_list = tk.Listbox(mw)
contact_list.pack(fill=tk.BOTH, expand=True)

# Run the application
mw.mainloop()
