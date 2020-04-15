from tkinter import *
from bs4 import BeautifulSoup
import requests

tk=Tk()
tk.title("Exchange rate PLN")
tk.resizable(False, False)

def returnEntry(arg=None):
    global ms
    ms = myEntry.get()
    if(ms==""):
        ms = 500
    myEntry.destroy()
    resultLabel.destroy()
    infoLabel.destroy()
    mainFunction()

resultLabel = Label(tk, text = "Enter the time to refresh the data in ms and press Enter (default 500ms): ")
resultLabel.pack()

myEntry = Entry(tk, width=20)
myEntry.focus()
myEntry.bind("<Return>",returnEntry)
myEntry.pack()

infoLabel = Label(tk, text = "If the value provided is not an integer the program will assign default value (500ms).")
infoLabel.pack()

url = 'https://www.nbp.pl/home.aspx?f=/kursy/kursyc.html'

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

def mainFunction():
    Label(tk, padx=5, pady=5, text="Name (Polish): ", bg="#006dbc", font="bold").grid(row=0, column=0)
    Label(tk, padx=5, pady=5, text="Code: ", bg="#006dbc", font="bold").grid(row=0, column=1)
    Label(tk, padx=5, pady=5, text="Sell: ", bg="#006dbc", font="bold").grid(row=0, column=2)
    Label(tk, padx=5, pady=5, text="Buy: ", bg="#006dbc", font="bold").grid(row=0, column=3)
 

    def getData():
        soup = BeautifulSoup(response.text, 'lxml')
        for s in soup.find_all('table', attrs={'class' : 'pad5'}):
            for row, tr in enumerate(s.find_all('tr')):
                for col, td in enumerate(tr.find_all('td')):
                    Label(tk, padx=5, pady=5, text=td.text).grid(row=row, column=col)
        print("Data updated after {}ms.".format(ms))
        tk.after(ms, getData)

    getData()

tk.mainloop()