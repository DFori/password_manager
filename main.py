from tkinter import *
BLUE = "#97DEFF"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(height=400, width=400, padx=50, pady=50, bg="black")


logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_lb = Label(text="website:", fg="white", bg="black", font=("Arial", 16))
website_lb.grid(column=0, row=1)

web_ent = Entry(width=35, bg="black", highlightthickness=0)
web_ent.grid(column=1, row=1, columnspan=2)
web_ent.focus()

name_lb = Label(text="Email/Username:", fg="white", bg="black", font=("Arial", 16))
name_lb.grid(column=0, row=2)

name_ent = Entry(width=35, bg="black", highlightthickness=0)
name_ent.grid(column=1, row=2, columnspan=2)

password_lb = Label(text="Password:", fg="white", bg="black", font=("Arial", 16))
password_lb.grid(column=0, row=3)

password_ent = Entry(width=18, bg="black", highlightthickness=0)
password_ent.grid(column=1, row=3)

password_btn = Button(text="Generate Password", highlightthickness=0, highlightbackground="black")
password_btn.grid(column=2, row=3)


add_btn = Button(text="Add", highlightthickness=0, highlightbackground="black", width=30)
add_btn.grid(column=1, row=4, columnspan=2)





window.mainloop()