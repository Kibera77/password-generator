'''

title: a simple password generator
Gui version  

'''


from tkinter import Toplevel, END, Label, Menu, Button, Text, Spinbox, Radiobutton, StringVar, Tk
from random import choice
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename

window = Tk()
window.geometry('800x500')
window.title('Fast Password Generator')

numbers = '0123456789'
alphanum = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_alpha_num = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'!@$%()?"


def create_pass():
    the_choice = type_choice.get()

    if the_choice == "":
        result_box.delete(0.0, END)

        result_box.insert(END, "\n Please select the password type to use...")

        messagebox.showerror('Error!','Cannot choose from an Empty Sequence!')

    length = int(pass_length.get())
    rand_pass = []
    for i in range(length):
        rand_pass.append(choice(the_choice))

    result = "".join(rand_pass)

    the_result = "\n *** Your password is: " + result + " *** \n "
    result_box.delete(0.0, END)
    result_box.insert(END, the_result)


# the menu
def click():
    print('Create a new file')


def tip():
    messagebox.showinfo('Coding', 'Did you know you can learn coding more easily and faster by just practicing often '

                                  'Other than just reading!')


def read():
    messagebox.askquestion('Querry', 'What do you want to know about the developer?')


def newWindow():
    root = Toplevel(window)
    root.geometry('600x600')
    root.title('New frame window')

    label = Label(root,text='dante', fg='blue', font=('arial', 18, 'bold'),bg='red')
    label.grid(row=0, column=0)

    root.mainloop()


def save_file():
    ''' save the current file as a new file '''

    file_path = asksaveasfilename(defaultextension='txt', filetypes=[('Text Files', '*.txt'), ('All files', '*.*')])
    if not file_path:
        return
    with open(file_path, 'w') as output_file:
        text = result_box.get('1.0', END)
        output_file.write(text)
    window.title(f'Password generator - {file_path}')


# the menyu files
menu_bar = Menu(window)
file = Menu(menu_bar, tearoff=0)
file.add_command(label='New File')
file.add_command(label='Open Folder')
file.add_command(label='Save')
file.add_command(label='Save As', command=save_file)
file.add_command(label='Close')

file.add_separator()

file.add_command(label='Exit', command=window.quit)
menu_bar.add_cascade(label='File', menu=file)

edit = Menu(menu_bar, tearoff=0)
edit.add_command(label='Undo')

edit.add_separator()

edit.add_command(label='Cut')
edit.add_command(label='Copy')
edit.add_command(label='Paste')
edit.add_command(label='Delete')
edit.add_command(label='Select')
edit.add_command(label='Select All')

menu_bar.add_cascade(label='Edit', menu=edit)

win = Menu(menu_bar, tearoff=0)
win.add_command(label='Store current layout as default')
win.add_command(label='Restore default layout')

win.add_separator()
win.add_command(label='Active')
win.add_command(label='Notifications')
win.add_command(label='Background tasks')
win.add_command(label='New tool window', command=newWindow)

menu_bar.add_cascade(label='Window', menu=win)

help = Menu(menu_bar, tearoff=0)
help.add_command(label='Help')

help.add_separator()

help.add_command(label='Find Action')
help.add_command(label='Getting started')
help.add_command(label='Tip of the Day', command=tip)

help.add_separator()
help.add_command(label='Contact support', command=read)
help.add_command(label='Submit a Bug report ')
help.add_command(label='Send us Feedback')
help.add_command(label='Collect logs and diagnostics data')

help.add_separator()
help.add_command(label='Check for updates')
help.add_command(label='About')

menu_bar.add_cascade(label='Help', menu=help)

# display the menu
window.config(menu=menu_bar)

''' Adding our widgets to the main application window
'''
author = Label(window, font=('sans serif', 8, 'italic'), text='Written by Dan', fg='red').place(relx=.4, rely=.97)
program_name = Label(window, font=('Helvetica', 20, 'bold'), text='Password Generator', fg='blue')
program_name.grid(row=1, column=2, padx=100, pady=30)

choose_type = Label(window, font=('arial', 15, 'bold'), text='Select password type')
choose_type.grid(row=4, column=1, padx=30)

type_choice = StringVar()

num_choice = Radiobutton(window, font=('arial', 10, 'normal'), text='Numeric', variable=type_choice, value=numbers)
num_choice.grid(row=5, column=1)

alphanum_choice = Radiobutton(window, font=('arial', 10, 'normal'), text='Alpha N', variable=type_choice,
                              value=alphanum)
alphanum_choice.grid(row=6, column=1)

special_num_choice = Radiobutton(window, font=('arial', 10, 'normal'), text='Special', variable=type_choice,
                                 value=special_alpha_num)
special_num_choice.grid(row=7, column=1)

size = Label(window, text='Size', font=('arial', 10, 'normal')).place(relx=.65, rely=.4)
pass_length = Spinbox(window, from_=8, to=40)
pass_length.place(relx=.72, rely=.4)
pass_length.config(state='readonly')

gen_btn = Button(window, text='Generate', fg='Blue', bg='#a5d0cf', command=create_pass)
gen_btn.place(relx=.42, rely=.57)

result_box = Text(window, height=6, width=70)
result_box.place(relx=.06, rely=.7)

window.mainloop()
