from tkinter import *
from project.tools.validator import Validator
from tkinter import messagebox
from project.tools.logger import Logger


def emergency_window(service):
    window = Tk()
    logger = Logger()

    logger.info(f"{service} window opened")

    window.geometry("400x400")
    window.title(service + " Emergency")
    window.configure(bg="gray26")

    if service == "Police 🚨":
        Label(window, text=service, bg="gray26", fg="royal blue1", font=("Helvetica", 20, "bold")).pack()
    if service == "Ambulance⚕️":
        Label(window, text=service, bg="gray22", fg="deepskyblue3", font=("Helvetica", 20, "bold")).pack()
    if service == "Fire Station 🚒":
        Label(window, text=service, bg="gray22", fg="red3", font=("Helvetica", 20, "bold")).pack()

    Label(window, text="Name & Family").place(x=152, y=45)
    name_entry = Entry(window)
    name_entry.place(x=115, y=70, height=20, width=150)

    Label(window, text="Phone").place(x=173, y=100)
    phone_entry = Entry(window)
    phone_entry.place(x=115, y=125, height=20, width=150)

    Label(window, text="Location").place(x=167, y=155)
    location_entry = Entry(window)
    location_entry.place(x=115, y=180, height=20, width=150)

    Label(window, text="Description").place(x=160, y=210)
    description_entry = Entry(window)
    description_entry.place(x=50, y=235, height=90, width=290)

    def submit():
        phone = phone_entry.get()
        name = name_entry.get()
        location = location_entry.get()
        description = description_entry.get()

        try:
            Validator.phone_validator(phone, "Invalid phone number !!! \n ( شماره معتبر نیست )")
            Validator.en_name_validator(name, "Invalid Name !!! \n ( نام معتبر نیست )")
            Validator.location_validator(location, "Invalid Location !!! \n ( آدرس معتبر نیست )")

            logger.info(
                "Service: {0} | Name: {1} | Phone: {2} | Location: {3} | Description: {4} ".format(service, name, phone, location, description))

            messagebox.showinfo("Success", f"{service} has been dispatched")

        except Exception as e:

            messagebox.showerror("Error", f"{e}")

    Button(window, background="lawn green", text="Submit", command=submit).place(x=135, y=350, width=120)
    window.mainloop()
