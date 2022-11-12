import tkinter as tk
from tkinter import Tk, Menu, Canvas
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
import tksvg

root = Tk()
root.geometry('800x600')
root.title('My Music')


# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

# add the File menu to the menubar
file_menu.add_cascade(
    label="Preferences",
    menu=sub_menu
)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu,
    underline=0
)

def show_selected_size():
    showinfo(
        title='Result',
        message=selected_size.get()
    )


selected_size = tk.StringVar()
sizes = (('C', 'C'),('C#', 'C#'),
         ('D', 'D'),('D#', 'D#'),
         ('E', 'E'),
         ('F', 'F'), ('F#', 'F#'),
         ('G', 'G'), ('G#', 'G#'),
         ('A', 'A'), ('A#', 'A#'),
         ('B', 'B'), ('B#', 'B#'),
         )

# label
label = ttk.Label(text="Select a tone")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size
    )
    r.pack(fill='x', padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Get Selected Size",
    command=show_selected_size)

button.pack(fill='x', padx=5, pady=5)


svg_image = tksvg.SvgImage('C:/tmp/my_music/circle.svg')
#label = tk.Label(image=svg_image)
#label.pack(fill='x', padx=5, pady=5)
frame=tk.Frame(root)
tk_image=svgPhotoImage('C:/tmp/my_music/circle.svg')
frame.configure(image=tk_image)

root.mainloop()
