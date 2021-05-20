from tkinter import *
from tkinter.ttk import *



def save():
    name = name_var.get()            
    phone= phone_var.get() 
    place= place_var.get() 
    temp= temperature_var.get() 
    with open("info.csv","a") as f:
            f.writelines(f'\n{name},{phone},{place},{temp}')
    f.close()

    name_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    place_entry.delete(0, 'end')
    temp_entry.delete(0, 'end')    

def close():
    root.destroy()

root = Tk()
root.geometry("700x700")
root.configure(bg="grey")
style = Style()

style.configure('TButton', font=
('calibri', 16),
                borderwidth='2')

name_var = StringVar()
phone_var = StringVar()
place_var = StringVar()

temperature_var = StringVar()
head_label = Label(root, text='Data-Logging', font=('calibre', 33, 'bold'))

name_label = Label(root, text='Name', font=('calibre', 20, 'bold'))
phone_label = Label(root, text='Phone Number', font=('calibre', 20, 'bold'))
place_label = Label(root, text='Place', font=('calibre', 20, 'bold'))
temp_label = Label(root, text='Temperature', font=('calibre', 20, 'bold'))

name_entry = Entry(root, textvariable=name_var, font=('calibre', 20, 'normal'))
phone_entry = Entry(root, textvariable=phone_var, font=('calibre', 20, 'normal'))
place_entry = Entry(root, textvariable=place_var, font=('calibre', 20, 'normal'))
temp_entry = Entry(root, textvariable=temperature_var, font=('calibre', 20, 'normal'))

sub_btn = Button(root, text='Submit', command=save)
close_btn = Button(root, text='Close', command=close)

head_label.grid(row=0, column=1,columnspan=2, pady=10)

name_label.grid(row=1, column=1, pady=10, padx=40)
name_entry.grid(row=1, column=2, pady=10, padx=10)

phone_label.grid(row=2, column=1, pady=10, padx=40)
phone_entry.grid(row=2, column=2, pady=10, padx=10)

place_label.grid(row=3, column=1, pady=10, padx=40)
place_entry.grid(row=3, column=2, pady=10, padx=10)

temp_label.grid(row=4, column=1, pady=10, padx=40)
temp_entry.grid(row=4, column=2, pady=10, padx=10)

sub_btn.grid(row=5, column=2, pady=20, padx=40)
close_btn.grid(row=5, column=1, pady=20, padx=40)


while True:
    root.update()