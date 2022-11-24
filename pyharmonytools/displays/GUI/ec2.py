import tkinter as tk
from io import BytesIO

from PIL.Image import Resampling
from svglib.svglib import svg2rlg
from PIL import Image, ImageTk
from reportlab.graphics import renderPM

root = tk.Tk()
root.title("Co5")
root.geometry("800x600")

svg_file = svg2rlg('/circle.svg')
byte_png = BytesIO()
renderPM.drawToFile(svg_file, byte_png, fmt="PNG")

c = tk.Button(text="Co5", width="400", height="400")
c.pack()

img = Image.open(byte_png)
img = img.resize((c.winfo_width(), c.winfo_height()), Resampling.LANCZOS)
img.image = img
img = ImageTk.PhotoImage(img)

c.configure(image=img)

root.mainloop()
