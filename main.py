import csv
import os
import random
import string
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime

first = True

def func_loop():
    make_csv()

def make_csv():
    def counter():
        enter_data()
        # Reset entry fields
        user_name_entry.delete(0, tk.END)
        user_last_entry.delete(0, tk.END)
        user_mail_entry.delete(0, tk.END)
        user_id_entry.delete(0, tk.END)
        user_pswd_entry.delete(0, tk.END)

    def ending():
        if enter_data():
            # Close the window
            window.destroy()
            messagebox.showinfo("Data Saved", "Data saved successfully!")
        else:
            messagebox.showinfo("Error", "Something went wrong ask JOHNNY!")
        
    def enter_data():
        global first

        guest_first = user_name_entry.get()
        guest_last = user_last_entry.get()
        guest_mail = user_mail_entry.get().replace(" ", "")
        guest_id = user_id_entry.get().replace(" ", "")
        guest_pswd = user_pswd_entry.get()

        spon_first = Sponso_name_entry.get()
        spon_last = Sponso_last_entry.get()
        spon_mail = Sponso_mail_entry.get().replace(" ", "")
        start_d = Sponso_start_entry.get()
        end_d = Sponso_end_entry.get()

        # Mail auto fill
        if guest_mail:
            guest_mail = guest_mail
        else:
            guest_mail = "nomail@please.com"
            tk.messagebox.showwarning(title="Auto Mail", message="Automatic mail is now: `nomail@please.com`")

         # Id auto fill
        if guest_id:
            guest_id = guest_id.get()
        else:
            last = guest_last.split()
            guest_id = guest_first[0] + "." + last[0]
            tk.messagebox.showwarning(title="Auto ID", message="ID = "+guest_id)

        # Pswd auto fill
        if guest_pswd:
            guest_pswd = user_pswd_entry.get()
        else:
            source = string.ascii_letters + string.digits
            guest_pswd = ''.join(random.choice(source) for i in range(10))
            tk.messagebox.showwarning(title="Auto Password", message="Password = "+guest_pswd)

        csv_file_path = "C:\\Wifi_Guest\\wifi.csv"

        # Parent Directory path 
        par_dir = "C:\\Wifi_Guest\\"
        pat = os.path.join(par_dir, "Pdf")
        if not os.path.exists(pat):
            os.mkdir(pat, 0o777)

        # Make PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = "Date : "+datetime.now().date().strftime("%Y-%m-%d"), ln = 1, align = 'R')
        pdf.cell(200, 10, txt = "     ", ln = 2, align = 'C')
        pdf.cell(200, 10, txt = "WIFI GUEST", ln = 3, align = 'C')
        pdf.cell(200, 10, txt = "     ", ln = 4, align = 'C')
        pdf.cell(200, 10, txt = "Start date = "+start_d+" => "+"End date = "+end_d, ln = 5, align = 'C')
        pdf.cell(200, 10, txt = "     ", ln = 6, align = 'C')
        pdf.cell(200, 10, txt = "User name = "+ guest_id +"                          "+"Password = "+guest_pswd, ln = 8, align = 'C')
        
        # Save PDF
        pdf.output(pat+"\\"+guest_id+".pdf")

        if guest_id and guest_first and guest_last and spon_first and spon_last and spon_mail:
            mode = 'a' if not first else 'w'
            with open(csv_file_path, mode, newline='') as file:
                writer = csv.writer(file)
                if mode == 'w':
                    writer.writerow(["Guest's First Name (Required),Guest's Last Name (Required),Guest's Email,Guest' Phone Number,Guest's ID,Guest's password,Sponsor's First Name,Sponsor's Last Name,Sponsor's Email"])
                writer.writerow([guest_first, guest_last, guest_mail, "", guest_id, guest_pswd, spon_first, spon_last, spon_mail])
            first = False
            return True
        else:
            tk.messagebox.showwarning(title="Error", message="Every fields with * are required. Please complete them.")
            return False

    def multi():
        if first == False:
            tk.messagebox.showwarning(title="Error", message="WRONG BUTTON SUPID BOI :')")
            return False
        
        if multi_num_entry.get() and multi_pswd_entry.get() and multi_pre_entry.get:

            # Taking in data
            number = int(multi_num_entry.get())
            multi_pass = multi_pswd_entry.get()
            prefix = multi_pre_entry.get().replace(" ", "")
            start_date = multi_start_entry.get()
            end_date = multi_end_entry.get()

            # Making Folder
            directory = prefix

            # Parent Directory path 
            parent_dir = "C:\\Wifi_Guest\\"
            path = os.path.join(parent_dir, directory)
            if not os.path.exists(path):
                os.mkdir(path, 0o777)
        
            with open("C:\\Wifi_Guest\\anonymous.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Guest's First Name (Required),Guest's Last Name (Required),Guest's Email,Guest' Phone Number,Guest's ID,Guest's password,Sponsor's First Name,Sponsor's Last Name,Sponsor's Email"])
                while number > 0:
                    # Make PDF
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size = 15)
                    pdf.cell(200, 10, txt = "Date : "+datetime.now().date().strftime("%Y-%m-%d"), ln = 1, align = 'R')
                    pdf.cell(200, 10, txt = "     ", ln = 2, align = 'C')
                    pdf.cell(200, 10, txt = "WIFI GUEST", ln = 3, align = 'C')
                    pdf.cell(200, 10, txt = "     ", ln = 4, align = 'C')
                    pdf.cell(200, 10, txt = "Start date = "+start_date+" => "+"End date = "+end_date, ln = 5, align = 'C')
                    pdf.cell(200, 10, txt = "     ", ln = 6, align = 'C')
                    pdf.cell(200, 10, txt = "User name = "+prefix+str(number)+"                          "+"Password = "+multi_pass, ln = 8, align = 'C')
                    # Save PDF
                    pdf.output(path+"\\"+prefix+str(number)+".pdf")

                    writer.writerow([prefix, prefix, "nomail@please.com", "", prefix+str(number), multi_pass, "Sponsor", "Sponsor", "nomail@please.com"])
                    number = number-1
        else:
            tk.messagebox.showwarning(title="Error", message="Every fields are required for anonymous guest. Please complete them.")
        # Close the window
        window.destroy()
        messagebox.showinfo("Data Saved", "Data saved successfully!")



    window = tk.Tk()
    img = PhotoImage(file='C:\\Wifi_Guest\\wifi.png')
    window.iconphoto(False, img)
    window.title("Wifi Guest - V1.69")

    logo_label = tk.Label(window, image=img)
    logo_label.grid(row=0, column=0, columnspan=2, pady=10)

    frame = tk.Frame(window)
    frame.grid(row=1, column=0)

    # Saving User Info
    user_info_frame = tk.LabelFrame(frame, text="Guest Info")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky="news")

    user_name_label = tk.Label(user_info_frame, text="First Name *")
    user_name_label.grid(row=0, column=0, sticky='nswe')
    user_name_entry = tk.Entry(user_info_frame)
    user_name_entry.grid(row=1, column=0, sticky='nswe')

    user_last_label = tk.Label(user_info_frame, text="Last Name *")
    user_last_label.grid(row=0, column=1, sticky='nswe')
    user_last_entry = tk.Entry(user_info_frame)
    user_last_entry.grid(row=1, column=1, sticky='nswe')

    user_mail_label = tk.Label(user_info_frame, text="Email\n(Leave this blank to auto generate)")
    user_mail_label.grid(row=0, column=2, sticky='nswe')
    user_mail_entry = tk.Entry(user_info_frame)
    user_mail_entry.grid(row=1, column=2, sticky='nswe')

    user_id_label = tk.Label(user_info_frame, text="ID\n(Leave this blank to auto generate)")
    user_id_label.grid(row=2, column=0, sticky='nswe')
    user_id_entry = tk.Entry(user_info_frame)
    user_id_entry.grid(row=3, column=0, sticky='nswe')

    user_pswd_label = tk.Label(user_info_frame, text="Password\n(Leave this blank to auto generate)")
    user_pswd_label.grid(row=2, column=1, sticky='nswe')
    user_pswd_entry = tk.Entry(user_info_frame)
    user_pswd_entry.grid(row=3, column=1, sticky='nswe')

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=50, pady=5, sticky='nswe')

    # Saving Sponsor Info
    sponsor_frame = tk.LabelFrame(frame, text="Sponsor Info")
    sponsor_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

    Sponso_name_label = tk.Label(sponsor_frame, text="First Name *")
    Sponso_name_label.grid(row=0, column=0, sticky='nswe')
    Sponso_name_entry = tk.Entry(sponsor_frame)
    Sponso_name_entry.grid(row=1, column=0, sticky='nswe')

    Sponso_last_label = tk.Label(sponsor_frame, text="Last Name *")
    Sponso_last_label.grid(row=0, column=1, sticky='nswe')
    Sponso_last_entry = tk.Entry(sponsor_frame)
    Sponso_last_entry.grid(row=1, column=1, sticky='nswe')

    Sponso_mail_label = tk.Label(sponsor_frame, text="Email *")
    Sponso_mail_label.grid(row=0, column=2, sticky='nswe')
    Sponso_mail_entry = tk.Entry(sponsor_frame)
    Sponso_mail_entry.grid(row=1, column=2, sticky='nswe')

    Sponso_start_label = tk.Label(sponsor_frame, text="Starting Date\nFormat : DD/MM/YYYY hh:mm")
    Sponso_start_label.grid(row=2, column=0, sticky='nswe')
    Sponso_start_entry = tk.Entry(sponsor_frame)
    Sponso_start_entry.grid(row=3, column=0, sticky='nswe')

    Sponso_end_label = tk.Label(sponsor_frame, text="Ending Date\nFormat : DD/MM/YYYY hh:mm")
    Sponso_end_label.grid(row=2, column=1, sticky='nswe')
    Sponso_end_entry = tk.Entry(sponsor_frame)
    Sponso_end_entry.grid(row=3, column=1, sticky='nswe')

    for widget in sponsor_frame.winfo_children():
        widget.grid_configure(padx=50, pady=5, sticky='nswe')

    # Button
    button = tk.Button(frame, text="Create CSV", command=ending)
    button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    add = tk.Button(frame, text="More Guest", command=counter)
    add.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    # For multiple guest creation

    multi_frame = tk.LabelFrame(frame, text="Multiple anonymous Guest Accounts")
    multi_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

    multi_num_label = tk.Label(multi_frame, text="Number of Accounts")
    multi_num_label.grid(row=0, column=0, sticky='nswe')
    multi_num_entry = tk.Entry(multi_frame)
    multi_num_entry.grid(row=1, column=0, sticky='nswe')

    multi_pswd_label = tk.Label(multi_frame, text="Password")
    multi_pswd_label.grid(row=0, column=1, sticky='nswe')
    multi_pswd_entry = tk.Entry(multi_frame)
    multi_pswd_entry.grid(row=1, column=1, sticky='nswe')

    multi_pre_label = tk.Label(multi_frame, text="User name prefix eg : Guest_")
    multi_pre_label.grid(row=0, column=2, sticky='nswe')
    multi_pre_entry = tk.Entry(multi_frame)
    multi_pre_entry.grid(row=1, column=2, sticky='nswe')

    multi_start_label = tk.Label(multi_frame, text="Starting Date\nFormat : DD/MM/YYYY hh:mm")
    multi_start_label.grid(row=2, column=0, sticky='nswe')
    multi_start_entry = tk.Entry(multi_frame)
    multi_start_entry.grid(row=3, column=0, sticky='nswe')

    multi_end_label = tk.Label(multi_frame, text="Ending Date\nFormat : DD/MM/YYYY hh:mm")
    multi_end_label.grid(row=2, column=1, sticky='nswe')
    multi_end_entry = tk.Entry(multi_frame)
    multi_end_entry.grid(row=3, column=1, sticky='nswe')


    for widget in multi_frame.winfo_children():
        widget.grid_configure(padx=50, pady=5, sticky='nswe')

    # Button multi
    button = tk.Button(frame, text="Create anonymous accounts", command=multi)
    button.grid(row=5, column=0, sticky="news", padx=20, pady=10)

    # Copyright section
    copyright_frame = tk.Frame(frame)
    copyright_frame.grid(row=6, column=0, pady=10)
    copyright_label = tk.Label(copyright_frame, text="© 2024 John Jeffrey PANINGBATAN. All rights reserved.")
    copyright_label.pack()

    window.mainloop()

func_loop()
