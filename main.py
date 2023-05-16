from tkinter import *
BLUE = "#97DEFF"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(height=400, width=400, padx=40, pady=40, bg="white")


logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_lb = Label(text="website:", fg="black", bg="white")
website_lb.grid(column=0, row=1)

web_txt = Text(bg="white", height=1, width=43, highlightthickness=2)
web_txt.grid(column=1, row=1, columnspan=2)

name_lb = Label(text="Email/Username:", fg="black", bg="white")
name_lb.grid(column=0, row=2)

name_txt = Text(bg="white", height=1, width=43, highlightthickness=2)
name_txt.grid(column=1, row=2, columnspan=2)

password_lb = Label(text="Password:", fg="black", bg="white")
password_lb.grid(column=0, row=3)

password_txt = Text(bg="white", height=1, width=21, highlightthickness=2)
password_txt.grid(column=1, row=3)

password_btn = Button(text="Generate Password", highlightthickness=0, highlightbackground="white")
password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", highlightthickness=0, highlightbackground="white", width=30)
add_btn.grid(column=1, row=4, columnspan=2)





window.mainloop()