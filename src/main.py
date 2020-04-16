from tkinter import *
from bs4 import BeautifulSoup
import requests

tk=Tk()
tk.title("Exchange rate PLN") #Set title
tk.resizable(False, False) #Blocking the window from resizable

def returnEntry(arg=None): #Assigning user input to the ms variable
    global ms
    
    #If the data is not int, ms = 500ms
    try: 
        ms = int(enterMS.get())
    except:
        ms = 500

    #Destroy unnecessary labels and entry
    enterMS.destroy()
    resultLabel.destroy()
    infoLabel.destroy()

    #Go to mainFunction()
    mainFunction()

resultLabel = Label(tk, text = "Enter the time to refresh the data in ms and press Enter (default 500ms): ")
resultLabel.pack()

enterMS = Entry(tk, width=20)
enterMS.focus()
enterMS.bind("<Return>",returnEntry)
enterMS.pack()

infoLabel = Label(tk, text = "If the value provided is not an integer the program will assign default value (500ms).")
infoLabel.pack()

#Set url with data
url = 'https://www.nbp.pl/home.aspx?f=/kursy/kursyc.html'

#Set headers
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

def mainFunction():
    #Information labels
    Label(tk, padx=5, pady=5, text="Name (Polish): ", bg="#006dbc", font="bold").grid(row=0, column=0)
    Label(tk, padx=5, pady=5, text="Code: ", bg="#006dbc", font="bold").grid(row=0, column=1)
    Label(tk, padx=5, pady=5, text="Sell: ", bg="#006dbc", font="bold").grid(row=0, column=2)
    Label(tk, padx=5, pady=5, text="Buy: ", bg="#006dbc", font="bold").grid(row=0, column=3)
 

    def getData():
        #Downloading data and print in labels
        soup = BeautifulSoup(response.text, 'lxml')
        for s in soup.find_all('table', attrs={'class' : 'pad5'}):
            for row, tr in enumerate(s.find_all('tr')):
                for col, td in enumerate(tr.find_all('td')):
                    Label(tk, padx=5, pady=5, text=td.text).grid(row=row, column=col)

        #print("Data updated after {}ms.".format(ms)) #Debug line

        tk.after(ms, getData) #Data refresh every x ms (default 500ms)

    getData() #Go to getData()

tk.mainloop()