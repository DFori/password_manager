from tkinter import *
from tkinter import messagebox
import PW_generator
import json
BLUE = "#97DEFF"
# ----------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = web_ent.get()
    email = name_ent.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No file data exists")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(message=f"The email for {website} is {email}\n and the password is {password}")
        else:
            messagebox.showinfo(message="No details for website exists")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password():
    global rand_password
    password_ent.insert(0, PW_generator.generate())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_ent.get()
    email = name_ent.get()
    password = password_ent.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if len(website) < 1 or len(password) < 1 or len(email) < 1:
        messagebox.showerror(title="Oops", message="Please do not leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                  f"\nPassword: {password} \nIs it ok to save? ")
        if is_ok:
            try:
                with open("data.json", 'r') as data_file:
                    # reading the data
                    data = json.load(data_file)
            except:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating the old data with new data
                data.update(new_data)

                    # writing/saving updated data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                messagebox.showinfo(message="saved successfully")
                web_ent.delete(0, END)
                password_ent.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(height=400, width=400, padx=50, pady=50, bg="black")


logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_lb = Label(text="Website:", fg="white", bg="black", font=("Arial", 16))
website_lb.grid(column=0, row=1)

web_ent = Entry(width=20, bg="black", highlightthickness=0)
web_ent.grid(column=1, row=1)
web_ent.focus()

name_lb = Label(text="Email/Username:", fg="white", bg="black", font=("Arial", 16))
name_lb.grid(column=0, row=2)

name_ent = Entry(width=37, bg="black", highlightthickness=0)
name_ent.insert(0, "danielfori04@gmail.com")
name_ent.grid(column=1, row=2, columnspan=2)

password_lb = Label(text="Password:", fg="white", bg="black", font=("Arial", 16))
password_lb.grid(column=0, row=3)

password_ent = Entry(width=20, bg="black", highlightthickness=0)
password_ent.grid(column=1, row=3)

password_btn = Button(text="Generate Password", highlightthickness=0, highlightbackground="black", command=password)
password_btn.grid(column=2, row=3)


add_btn = Button(text="Add", highlightthickness=0, highlightbackground="black", width=34, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", highlightbackground="black", highlightthickness=0, width=13, command=find_password)
search_btn.grid(column=2, row=1)





window.mainloop()