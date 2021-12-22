import requests
import json
from tkinter import *

root = Tk()
root.title("Covid-19")
root.geometry("300x80")

# Including labels
lbl_1 = Label(root, text="Total confirmed cases: N/A", anchor="e")
lbl_2 = Label(root, text="Total dead cases: N/A", anchor="e")
lbl_3 = Label(root, text="Total recovered cases: N/A", anchor="e")

lbl_1.grid(column=1, row=0)
lbl_2.grid(column=1, row=1)
lbl_3.grid(column=1, row=2)


def clicked():
    # Opening the url and loading the
    # json data using json Library
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    text_cases = f'Cases: {"{:,}".format(int(data["cases"]))}'
    text_deaths = f'Deaths: {"{:,}".format(int(data["deaths"]))}'
    text_recovered = f'Recoveries: {"{:,}".format(int(data["recovered"]))}'

    lbl_1.configure(text="Total confirmed cases: " + text_cases)
    lbl_2.configure(text="Total death cases: " + text_deaths)
    lbl_3.configure(text="Total recovered cases: " + text_recovered)


btn = Button(root, text="Refresh", command=clicked)
btn.grid(column=1, row=3)

root.mainloop()
