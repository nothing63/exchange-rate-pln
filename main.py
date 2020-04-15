from tkinter import *
from bs4 import BeautifulSoup
import requests

tk=Tk()
tk.title("Exchange rate PLN")
tk.resizable(False, False)

Label(tk, padx=5, pady=5, text="Name (Polish): ", bg="#006dbc", font="bold").grid(row=0, column=0)
Label(tk, padx=5, pady=5, text="Code: ", bg="#006dbc", font="bold").grid(row=0, column=1)
Label(tk, padx=5, pady=5, text="Sell: ", bg="#006dbc", font="bold").grid(row=0, column=2)
Label(tk, padx=5, pady=5, text="Buy: ", bg="#006dbc", font="bold").grid(row=0, column=3)

url = 'https://www.nbp.pl/home.aspx?f=/kursy/kursyc.html'
 
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
 
soup = BeautifulSoup(response.text, 'lxml')
for s in soup.find_all('table', attrs={'class' : 'pad5'}):
    for row, tr in enumerate(s.find_all('tr')):
        for col, td in enumerate(tr.find_all('td')):
            Label(tk, padx=5, pady=5, text=td.text).grid(row=row, column=col)

tk.mainloop()