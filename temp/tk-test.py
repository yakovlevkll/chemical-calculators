import tkinter as tk
import tkinter.font as tkFont

from PIL import ImageTk, Image


def test():
    print(1)


def calc(_event=None):
    # res = eval(expression)
    label1["text"] = data.get()


def close(_event=None):
    root.quit()


def fontSettings(fontsize=12):
    default_font = tkFont.nametofont("TkDefaultFont")
    text_font = tkFont.nametofont("TkTextFont")
    fixed_font = tkFont.nametofont("TkFixedFont")

    default_font.configure(size=fontsize)
    text_font.configure(size=fontsize)
    fixed_font.configure(size=fontsize)


# my_font = tkFont.Font(size=20)


root = tk.Tk()

frame = tk.LabelFrame(root, text="Some label")

frame.grid(row=1, column=1, pady=5, padx=5)

frame2 = tk.LabelFrame(root, text="Some label 2")

frame2.grid(row=1, column=2, pady=5, padx=5)

fontSettings()

padding = {"padx": 10, "pady": 10}


def metric_changed():
    metricChanged


measureSystem = tk.StringVar()
check = tk.Checkbutton(
    frame,
    text="select one",
    command=metric_changed,
    variable=measureSystem,
    onvalue="metric",
    offvalue="imperial",
)
check.grid(row=3, column=3, ipady=2, **padding)

button_submit = tk.Button(frame, text="Submit",
                          command=calc, font=("Helvetica", "30"))
button_submit.grid(row=1, columnspan=2, ipady=10)

button_submit2 = tk.Button(
    frame2, text="Submit", command=calc, font=("Helvetica", "30")
)
button_submit2.grid(row=1, columnspan=2, ipady=10)


label1 = tk.Label(frame, text="Some label")  # set your text
label1.grid(row=1, column=3, ipady=3, **padding)

data = tk.StringVar()

entry = tk.Entry(frame, textvariable=data)
entry.grid(row=2, column=1)
root.bind("<Return>", calc)

button_close = tk.Button(frame, text="Close", command=close)
button_close.grid(row=5, columnspan=2)


def select_close_button(_event=None):
    button_close.focus()


root.bind("<q>", select_close_button)
button_close.bind("<Return>", close)


def add_image(path, label):
    img_obj = Image.open(path)
    img = ImageTk.PhotoImage(img_obj)
    label["image"] = img


img_obj = Image.open("./Moscow.jpg")
path = "../../../Moscow.jpg"
img = ImageTk.PhotoImage(img_obj)

label2 = tk.Label(frame, image=img)  # set your text
label2.grid(row=4, column=3, ipady=3, padx=15, pady=18)

# add_image("./Moscow.jpg", label2)


root.mainloop()
