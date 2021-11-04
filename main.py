# Updated version
from tkinter import *
from tkinter.ttk import *
import requests
import json
from time import sleep


def screen():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    text_cases = f'Cases: {"{:,}".format(int(data["cases"]))}'
    text_deaths = f'Deaths: {"{:,}".format(int(data["deaths"]))}'
    text_recovered = f'Recoveries: {"{:,}".format(int(data["recovered"]))}'
    label.config(text=(f"{text_cases}\n{text_deaths}\n{text_recovered}"))
    label.after(1000, screen)


root = Tk()
root.title("CoronaInf4mation")

notebook = Notebook(root)
notebook.pack(paddy=15)

tab_all = Frame(notebook, width=100, height=100).pack(fill="both", expand=True)
tab_vietnam = Frame(notebook, width=100, height=100).pack(fill="both", expand=True)


label = Label(root, font=("sans", 80), background="grey", foreground="black")
label.pack(anchor="center")
screen()
root.mainloop()