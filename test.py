# Updated version
from tkinter import *
from tkinter.ttk import *
import requests
import json
from time import sleep

root = Tk()
root.title("CoronaInf4mation")

notebook = Notebook(root)
notebook.pack(pady=15)

tab_all = Frame(notebook, width=100, height=100)
tab_vietnam = Frame(notebook, width=100, height=100)

tab_vietnam.pack(fill="both", expand=1)
tab_all.pack(fill="both", expand=1)


notebook.add(tab_all, text="Global")
notebook.add(tab_vietnam, text="Vietnam")


def screen_vietnam():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/countries/vietnam")
    data = r.json()
    text_cases = f'Cases: {"{:,}".format(int(data["cases"]))}'
    text_deaths = f'Deaths: {"{:,}".format(int(data["deaths"]))}'
    text_recovered = f'Recoveries: {"{:,}".format(int(data["recovered"]))}'
    label_vietnam.config(text=(f"{text_cases}\n{text_deaths}\n{text_recovered}"))
    label_vietnam.after(1000, screen_vietnam)


def screen_all():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    text_cases = f'Cases: {"{:,}".format(int(data["cases"]))}'
    text_deaths = f'Deaths: {"{:,}".format(int(data["deaths"]))}'
    text_recovered = f'Recoveries: {"{:,}".format(int(data["recovered"]))}'
    label_all.config(text=(f"{text_cases}\n{text_deaths}\n{text_recovered}"))
    label_all.after(1000, screen_all)


label_vietnam = Label(
    tab_vietnam,
    font=("sans", 80),
    background="grey",
    foreground="black",
    width=200,
)
label_all = Label(
    tab_all,
    font=("sans", 80),
    background="grey",
    foreground="black",
    width=200,
)

label_vietnam.pack(anchor="center")
label_all.pack(anchor="center")

screen_vietnam()
screen_all()

root.mainloop()
