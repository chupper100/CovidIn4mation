#Updated version
from tkinter import*
from tkinter.ttk import*
import requests
import json

def screen():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    text_cases=f'Cases: {data["cases"]}'
    text_deaths=f'Deaths: {data["deaths"]}'
    text_recovered=f'Recovered: {data["recovered"]}'
    label.config(text=(f'{text_cases}\n{text_deaths}\n{text_recovered}'))
    label.after(1000, screen)

root = Tk()
root.title = "CoronaInf4mation"

label = Label(root,font=("sans",80),background='grey',foreground='black')
label.pack(anchor='center')
screen()
root.mainloop()