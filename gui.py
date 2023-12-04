# coming soon

import tkinter as tk

def guiStart():
    root = tk.Tk()

    root.geometry("250x340")
    root.title("Login")

    username_label = tk.Label(root, text="Input Username")
    username_label.pack()

    username_input_var = tk.StringVar()
    username_input = tk.Entry(root, textvariable=username_input_var)
    username_input.insert(0,"@")
    username_input.pack()

    def submit(username):
        result = username
        root.result = result # saves a variable result in root. idk why that works tbh
        root.destroy()

    username_button = tk.Button(root, text="Submit", command=lambda: submit(username_input_var.get()))
    username_button.pack()

    root.wait_window()
    return root.result


