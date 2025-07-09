from tkinter import *
from tkinter import ttk
import requests # type: ignore

climate = ""
def data_get():
    city = cityname.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=095310db0ceddcffe5b60b7c9114a3bf").json()
    cl_label1.config(text =data["weather"][0]["main"])
    tmp_label1.config(text =str(data["main"]["temp"]-273))
    hum_label1.config(text =str(data["main"]["humidity"]))

root = Tk()
root.title("Sid Weather")
root.config(bg = "light green")
root.geometry("650x430")

name_label = Label(root,text="SID Weather Display",bg="light green",font =("Arial",30,"bold"))
name_label.pack(pady=10)

cityname = StringVar()
com = ttk.Combobox(root,text="SID Weather Display",textvariable=cityname,font =("Arial",20,"bold"))
com.pack(pady=10)
done = Button(root,text="Get Weather",font = ("Arial",13,"bold"),command=data_get)
done.pack(pady=10)

cl_label = Label(root,text="Climate :"+climate,bg="light green",font =("Arial",10,"bold"))
cl_label.pack(pady=5)
cl_label1 = Label(root,text="",bg="White",font =("Arial",10,"bold"))
cl_label1.pack(pady=5)

tmp_label = Label(root,text="Temprature :",bg="light green",font =("Arial",10,"bold"))
tmp_label.pack(pady=5)
tmp_label1 = Label(root,text="",bg="white",font =("Arial",10,"bold"))
tmp_label1.pack(pady=5)

hum_label = Label(root,text="Humidity :",bg="light green",font =("Arial",10,"bold"))
hum_label.pack(pady=5)
hum_label1 = Label(root,text="",bg="white",font =("Arial",10,"bold"))
hum_label1.pack(pady=5)




root.mainloop()
