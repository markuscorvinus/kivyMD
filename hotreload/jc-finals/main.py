import tkinter as tk
from tkinter import messagebox
import random
from tkinter import *

def submit(name_entry, age_entry, checkin_entry, checkout_entry):
    # Get the user input from the entries
    name = name_entry.get()
    age = age_entry.get()
    checkin_date = checkin_entry.get()
    checkout_date = checkout_entry.get()

    # Validate the user input
    if not all(c.isalpha() or c.isspace() for c in name):
        messagebox.showerror("Error[NAME]", "Please remove symbols and numbers")
        return
    elif len(name) > 64:
        messagebox.showerror("Error[NAME]", "Name can only be up to 16 characters long.")
        return

    if not all(c.isnumeric() for c in age):
        messagebox.showerror("Error[AGE]", "ONLY NUMERIC 1-99")
        return
    elif len(age) > 2:
        messagebox.showerror("Error[AGE]", "INVALID AGE")
        return

    if all(c.isalpha() for c in checkin_date):
        messagebox.showerror("Error[CI/CO]", "FOLLOW THE FORMAT")
        return

    # Read the existing entries from the check-in text file
    entries = []
    try:
        with open("check-in.txt", "r") as file:
            for line in file:
                entries.append(line.strip())
    except FileNotFoundError:
        pass

    # Calculate the ID of the new entry
    if entries:
        last_entry_id = int(entries[-1].split("-")[0].replace("[", "").replace("]", ""))
        new_entry_id = f"[{last_entry_id+1}]"
    else:
        new_entry_id = "[1]"

    # Generate a random room number between 1 and 100
    room = random.randint(1, 100)

    # Save the assigned room number to a separate text file
    with open("room_lists.txt", "a") as file:
        file.write(f"{room}\n")

    # Show a receipt with the user's information and the assigned room number
    receipt = f"Name: {name}\nAge: {age}\nCheck-in Date: {checkin_date}\nCheck-out Date: {checkout_date}\nRoom Number: {room}\n\n*******************************************************\n[THIS SERVES AS YOUR RECEIPT, KINDLY TAKE A SCREENSHOT AND PRESENT IT TO THE FRONTDESK, THANK YOU!]"
    messagebox.showinfo("Receipt", receipt)

    # Save the input to the check-in text file with the assigned room number
    with open("check-in.txt", "a") as file:
        file.write(f"{new_entry_id}-NAME: [{name}], CI:[{checkin_date}], CO:[{checkout_date}], ROOM NO: [{room}]\n")

    # Print a success message
    print("Check-in successful.")
    
def create():
    # Create a new window
    create_window = tk.Toplevel()
    create_window.title("CHECK-IN")
    create_window.geometry("1920x1080")

    bg_image = tk.PhotoImage(file="7.png")

    bg_label = tk.Label(create_window, image=bg_image)
    bg_label.place(relx=0.5, rely=0.5, anchor="center")

    # Add a label 
    name_label = tk.Label(bg_label, text="PLEASE FILL IN THE FOLLOWING:", font=("Arial", 20, "bold"), fg="white", bg="black")
    name_label.place(relx=0.5, rely=0.1, anchor="center")

    # Add a label and entry for the name
    name_entry_label = tk.Label(bg_label, text="Full Name:", font=("Arial", 20, "bold"),fg="white", bg="black")
    name_entry_label.place(relx=0.5, rely=0.25, anchor="center")

    name_entry = tk.Entry(bg_label, font=("Arial", 14))
    name_entry.place(relx=0.5, rely=0.3, anchor="center",width=400, height=50)

    # Add a label and entry for the age
    age_entry_label = tk.Label(bg_label, text="Age:", font=("Arial", 20, "bold"),fg="white", bg="black")
    age_entry_label.place(relx=0.5, rely=0.35, anchor="center")

    age_entry = tk.Entry(bg_label, font=("Arial", 14))
    age_entry.place(relx=0.5, rely=0.4, anchor="center",width=100, height=50)

    # Add a label and entry for the check-in date
    checkin_entry_label = tk.Label(bg_label, text="Check-in Date (YYYY-MM-DD):", font=("Arial", 20,"bold"),fg="white", bg="black")
    checkin_entry_label.place(relx=0.5, rely=0.45, anchor="center")

    checkin_entry = tk.Entry(bg_label, font=("Arial", 14))
    checkin_entry.place(relx=0.5, rely=0.5,anchor="center",width=400, height=50)

    # Add a label and entry for the check-out date
    checkout_entry_label = tk.Label(bg_label, text="Check-out Date (YYYY-MM-DD):", font=("Arial", 20, "bold"),fg="white", bg="black")
    checkout_entry_label.place(relx=0.5, rely=0.55, anchor="center")

    checkout_entry = tk.Entry(bg_label, font=("Arial", 14))
    checkout_entry.place(relx=0.5, rely=0.6,anchor="center",width=400, height=50)

    room_entry_label = tk.Label(bg_label, text="Choose Room:", font=("Arial", 20, "bold"),fg="white", bg="black")
    room_entry_label.place(relx=0.5, rely=0.65, anchor="center")
    room_entry_label = tk.Label(bg_label, text="Note: Select from the table", font=("Arial", 10, "bold"),fg="white", bg="red")
    room_entry_label.place(relx=0.5, rely=0.685, anchor="center")

    room_entry = tk.Entry(bg_label, font=("Arial", 14))
    room_entry.place(relx=0.5, rely=0.728,anchor="center",width=100, height=50)

    # Add a submit button
    submit_button = tk.Button(bg_label, text="< BACK", command=create_window.destroy, font=("Arial", 14,"bold"), height=3, width=20)
    submit_button.place(relx=0.35, rely=0.82, anchor="w")

    submit_button = tk.Button(bg_label, text="Submit >", command=lambda: submit(name_entry, age_entry, checkin_entry, checkout_entry), font=("Arial", 14,"bold"), height=3, width=20)
    submit_button.place(relx=0.65, rely=0.82, anchor="e")

    # Add an exit button
   

    create_window.mainloop()
   
def view_customers():
    # Create a new window for displaying the list of customers
    view_window = tk.Toplevel()
    view_window.title("List of Customers")
    view_window.geometry("1920x1080")

    bg_image = tk.PhotoImage(file="7.png")

    bg_label = tk.Label(view_window, image=bg_image)
    bg_label.place(relx=0.5, rely=0.5, anchor="center")

    # Add a label with the player name
    name_label = tk.Label(bg_label, text="GUESTS INFORMATION:", font=("Arial", 20, "bold"), fg="white", bg="black")
    name_label.place(relx=0.5, rely=0.1, anchor="center")

    # Create a Text widget to display the list of customers
    entries_text = tk.Text(view_window, height=35, width=120, state="disabled")
    entries_text.place(relx=0.5,rely=0.41, anchor="center")

    # Read the entries from the file and insert them into the Text widget
    try:
        with open("check-in.txt", "r") as file:
            for line in file:
                entries_text.configure(state="normal")
                entries_text.insert("end", line)
                entries_text.configure(state="disabled")
    except FileNotFoundError:
        pass


    submit_button = tk.Button(bg_label, text="< BACK", command=view_window.destroy, font=("Arial", 14), height=3, width=20)
    submit_button.place(relx=0.5, rely=0.82, anchor="center")

    view_window.mainloop()


def check_room_availability():
    occupied_rooms = []
    try:
        with open("room_lists.txt", "r") as file:
            for line in file:
                room = line.strip()
                if room.isdigit():
                    occupied_rooms.append(int(room))
    except FileNotFoundError:
        pass
    
    # Create a new window to display the available rooms
    availability_window = tk.Toplevel()
    availability_window.title("Available Rooms")
    availability_window.geometry("1920x1080")

    bg_image = tk.PhotoImage(file="7.png")

    bg_label = tk.Label(availability_window, image=bg_image)
    bg_label.place(relx=0.5, rely=0.5, anchor="center")

    name_label = tk.Label(bg_label, text="ROOM AVAILABILITY:", font=("Arial", 20, "bold"), fg="white", bg="black")
    name_label.place(relx=0.5, rely=0.1, anchor="center")

    # Create a textbox to display the available rooms
    text_box = tk.Text(availability_window, height=35, width=120)
    text_box.place(relx=0.5,rely=0.41, anchor="center")
    
    for i in range(1, 101):
        if i in occupied_rooms:
            text_box.insert(tk.END, f"ROOM[{i}] - NOT AVAILABLE\n")
            text_box.tag_add("unavailable", f"{i}.0", f"{i}.end")
            text_box.tag_config("unavailable", foreground="red")
        else:
            text_box.insert(tk.END, f"ROOM[{i}] - AVAILABLE\n")
            text_box.tag_add("available", f"{i}.0", f"{i}.end")
            text_box.tag_config("available", foreground="green")
            
    text_box.config(state="disabled")

    submit_button = tk.Button(bg_label, text="< BACK", command=availability_window.destroy, font=("Arial", 14), height=3, width=20)
    submit_button.place(relx=0.5, rely=0.82, anchor="center")
    availability_window.mainloop()

def delete_entry():
    # Create a new window with a text box for user input and a submit button
    delete_window = tk.Toplevel()
    delete_window.title("Delete Entry")
    delete_window.geometry("1920x1080")

    bg_image = tk.PhotoImage(file="7.png")

    bg_label = tk.Label(delete_window, image=bg_image)
    bg_label.place(relx=0.5, rely=0.5, anchor="center")

    name_label = tk.Label(bg_label, text="ROOM AVAILABILITY:", font=("Arial", 20, "bold"), fg="white", bg="black")
    name_label.place(relx=0.5, rely=0.1, anchor="center",)


    room_label = Label(delete_window, text="ENTER ROOM NUMBER: ", font=("Arial", 20, "bold"), fg="white", bg="black")
    room_label.place(relx=0.5, rely=0.3, anchor="center")

    room_entry = Entry(delete_window, font=("Arial", 18))
    room_entry.place(relx=0.5, rely=0.4, anchor="center", width=100, height=50)

    submit_button = Button(delete_window, text="Submit", command=lambda: delete_entry_submit(room_entry.get()), font=("Arial", 14, "bold"), height=3, width=20)
    submit_button.place(relx=0.5, rely=0.55, anchor="center")
    submit_button = Button(delete_window, text="VIEW GUESTS", command=lambda: view_customers(), font=("Arial", 14, "bold"), height=3, width=20)
    submit_button.place(relx=0.5, rely=0.7, anchor="center")


    delete_window.mainloop()

def delete_entry_submit(room):
    # Read the existing entries from the check-in text file
    entries = []
    with open("check-in.txt", "r") as file:
        for line in file:
            entries.append(line.strip())

    # Find the entry with the room number entered by the user and remove it
    new_entries = []
    deleted = False
    for entry in entries:
        if f"ROOM NO: [{room}]" in entry:
            deleted = True
            continue
        new_entries.append(entry)

    # If the entry was not found, show an error message and return
    if not deleted:
        messagebox.showerror("Error", "Entry not found.")
        return

    # Write the updated entries back to the check-in text file
    with open("check-in.txt", "w") as file:
        file.write("\n".join(new_entries))

    # Read the existing room numbers from the room lists text file
    rooms = []
    with open("room_lists.txt", "r") as file:
        for line in file:
            rooms.append(int(line.strip()))

    # Remove the room number entered by the user from the list of rooms
    rooms.remove(int(room))

    # Write the updated list of rooms back to the room lists text file
    with open("room_lists.txt", "w") as file:
        file.write("\n".join(str(room) for room in rooms))

    # Show a success message
    messagebox.showinfo("Success", "Thank you and See You Again Soon!")


def submit_form():
    # Get the name from the form
    name = name_entry.get().upper()

    # Check if name is valid
    if not all(c.isalpha() or c.isspace() for c in name):
        messagebox.showerror("Error", "Please remove symbols and numbers")
        return
    elif len(name) > 16:
        messagebox.showerror("Error", "Name can only be up to 16 characters long.")
        return

    # Create a new window for the game selection
    game_window = tk.Toplevel()
    game_window.title("Select a Game")
    game_window.geometry("1920x1080")

    bg_image = tk.PhotoImage(file="7.png")
    bg_label = tk.Label(game_window, image=bg_image)
    bg_label.place(relx=0.5, rely=0.5, anchor="center")


    # Add a label with the player name
    name_label = tk.Label(game_window, text=f"WELCOME {name}!", font=("Arial", 40, "bold"),fg="white", bg="black")
    name_label.place(relx=0.5, rely=0.05, anchor="center")
    name_label = tk.Label(game_window, text=f"What can I do for you?", font=("Arial", 20, "bold"),fg="white", bg="black")
    name_label.place(relx=0.5, rely=0.1, anchor="center")
    
    # Add a button for the color game
    register_button = tk.Button(game_window, text="REGISTER", command=lambda: create(), font=("Arial", 14, "bold"), height=3, width=20)
    register_button.place(relx=0.5, rely=0.3, anchor="center")

    # Add a button for the tic-tac-toe game
    list_button = tk.Button(game_window, text="LIST OF GUESTS", command=lambda: view_customers(), font=("Arial", 14, "bold"), height=3, width=20)
    list_button.place(relx=0.5, rely=0.43, anchor="center")

    # Add a button for the leaderboards
    available_rooms_button = tk.Button(game_window, text="AVAILABLE ROOMS", command=lambda:check_room_availability(), font=("Arial", 14, "bold"), height=3, width=20)
    available_rooms_button.place(relx=0.5, rely=0.56, anchor="center")

    checkout_button = tk.Button(game_window, text="CHECK-OUT", command=lambda: delete_entry(), font=("Arial", 14, "bold"), height=3, width=20)
    checkout_button.place(relx=0.5, rely=0.69, anchor="center")

    exit_button = tk.Button(game_window, text="EXIT", command=game_window.destroy, font=("Arial", 14, "bold"), height=3, width=20)
    exit_button.place(relx=0.5, rely=0.82, anchor="center")

    game_window.mainloop()
    


# Create a new window for the form
form_window = tk.Tk()
form_window.title("Player Name")
form_window.geometry("1920x1080")

# Add a background image
bg_image = tk.PhotoImage(file="7.png")
bg_label = tk.Label(form_window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Add a label for the name field
name_label = tk.Label(form_window, text="PODS AND CAPSULE HOTEL MNL.", font=("Arial", 45, "bold"),fg="white", bg="black")
name_label.place(relx=0.5, rely=0.1, anchor="center")
name_label = tk.Label(form_window, text="Entertainment City, 1 Aseana Ave, Tambo, Parañaque, 1701 Metro Manila", font=("Arial", 11, "bold"), fg="white", bg="black")
name_label.place(relx=0.5, rely=0.15, anchor="center")

name_label = tk.Label(form_window, text="HOTEL RESERVATION MANAGEMENT", font=("Arial", 30, "bold"), fg="white", bg="black")
name_label.place(relx=0.5, rely=0.4, anchor="center")
name_label = tk.Label(form_window, text="Please Enter Your Name:", font=("Arial", 15, "bold"), fg="white", bg="black")
name_label.place(relx=0.5, rely=0.44, anchor="center")

# Add a text field for the name
name_entry = tk.Entry(form_window, font=("Arial", 18),)
name_entry.place(relx=0.5, rely=0.52, anchor="center", width=800, height=80)

# Add a button to submit the form
submit_button = tk.Button(form_window, text="> PROCEED <", command=submit_form, font=("Arial", 14, "bold"), height=3, width=20)
submit_button.place(relx=0.5, rely=0.7, anchor="center")

# Start the event loop
form_window.mainloop()