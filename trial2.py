import customtkinter
from tkinter import *
import requests
root=Tk()
root.geometry('300x300')
root.title("Smart Home Solution")

BLYNK_AUTH_TOKEN = 'nk24hJbhlmcJv9x6n8E49fH-Nx7sMrRb'
BLYNK_URL = f'https://blynk.cloud/external/api/'
def update_sensors():
    response_hum = requests.get(f'https://blynk.cloud/external/api/get?token=nk24hJbhlmcJv9x6n8E49fH-Nx7sMrRb&v5')
    if response_hum.status_code == 200:
        humidity_v5=float(response_hum.json())
        humidity_label.configure(text=f'Humidity : {humidity_v5}')

    response_temp = requests.get(f'https://blynk.cloud/external/api/get?token=nk24hJbhlmcJv9x6n8E49fH-Nx7sMrRb&v6')
    if response_temp.status_code == 200:
        temp_v6=float(response_temp.json())
        temp_label.configure(text=f'Temperature : {temp_v6}')

def update_cont():
    update_sensors()
    root.after(3000,update_cont)

humidity_label=customtkinter.CTkLabel(root,text="humidity")
humidity_label.pack()
temp_label=customtkinter.CTkLabel(root,text="temp")
temp_label.pack()

update_cont()

root.mainloop()