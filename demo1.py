from tkinter import *
import psutil
import math
import speedtest
from PIL import Image, ImageTk

def usage():
    cpu_count = psutil.cpu_count()
    cpu_count_label.config(text=cpu_count, image=tk_image, compound="center", fg="#00FF00")

    cpu_usage = psutil.cpu_percent(1)
    cpu_usage_label.config(text=cpu_usage, image=tk_image, compound="center", fg="#00FF00")
    cpu_usage_label.after(100, usage)

    ram_count = math.floor(psutil.virtual_memory()[0]/1000000000)
    ram_count_text = str(ram_count) + "Gb"
    ram_count_label.config(text=ram_count_text, image=tk_image, compound="center", fg="#00FF00")

    #RAM usage
    ram_usage = psutil.virtual_memory()[2]
    ram_usage_text = str(ram_usage) + "%"
    ram_usage_label.config(text=ram_usage_text, image=tk_image, compound="center", fg="#00FF00")

    ram_available = math.floor(psutil.virtual_memory()[1]/1000000000)
    ram_available_text = str(ram_available) + "Gb"
    ram_available_label.config(text=ram_available_text, image=tk_image, compound="center", fg="#00FF00")

def internet_speed():
    print("Testing internet speed")
    st = speedtest.Speedtest()
    download_speed = str(math.floor(st.download() / 1000000)) + "Mb/s"
    upload_speed = str(math.floor(st.upload() / 1000000)) + "Mb/s"
    ping = str(st.results.ping) + "ms"
    upload_label.config(text=upload_speed)
    download_label.config(text=download_speed)
    ping_label.config(text=ping)

root = Tk()
root.config(bg="black")
image = Image.open("blank_speedmeter.png")
tk_image = ImageTk.PhotoImage(image)

root.geometry("1500x1080")
root.title("CPU status")

#Creating label (the convencion of creating label is between the title and main loop)
#cpu count
cpu_count_label = Label(root,font=("Orbitron", 40, "bold"), text='0', bd=-4)
cpu_count_label.grid(row=0, column=0)
l1 = Label(root, font=("Orbitron", 20, "bold"),bg="black", fg="#00FF00" ,text="CPUs")
l1.grid(row=1,column=0)


#cpu usage
cpu_usage_label = Label(root,font=("Orbitron", 40, "bold"), text="0", bd=-4)
cpu_usage_label.grid(row=0, column=1)
l2 = Label(root, font=("Orbitron", 20, "bold"),bg="black", fg="#00FF00" ,text="CPU Usage in %")
l2.grid(row=1,column=1)

#Total RAM
ram_count_label = Label(root, font=("Orbitron", 40, "bold"), text="0", bd=-4)
ram_count_label.grid(row=0,column=2)
l3 = Label(root,  font=("Orbitron", 20, "bold"),bg="black", fg="#00FF00" ,text="Total RAM")
l3.grid(row=1,column=2)

#Ram % usage
ram_usage_label = Label(root, font=("Orbitron", 40, "bold"), text="0", bd=-4)
ram_usage_label.grid(row=0,column=3)
l4 = Label(root, font=("Orbitron", 20, "bold"),bg="black", fg="#00FF00" , text="RAM % Usage")
l4.grid(row=1,column=3)

#Available RAM
ram_available_label = Label(root,font=("Orbitron", 40, "bold"), text="0", bd=-4)
ram_available_label.grid(row=0, column=4)
l5 = Label(root, font=("Orbitron", 20, "bold"),bg="black", fg="#00FF00" , text="Available RAM")
l5.grid(row=1, column=4)

speed_button = Button(root,text="Test internet speed",bg="#00FF00" ,width=15, height=2 , font=("Orbitron", 15, "bold") , command=internet_speed)
speed_button.grid(row=3, column=0)

download_label = Label(root, font=("Orbitron", 30, "bold"), text="0 Mb/s", image=tk_image, compound="center", fg="#00FF00", bd=-4)
download_label.grid(row=3, column=1)
l6 = Label(root, font=("Orbitron", 20, "bold"),bg="black", fg="#00FF00" , text="Download Speed")
l6.grid(row=4, column=1)

upload_label = Label(root, font=("Orbitron", 30, "bold"), text="0 Mb/s", image=tk_image, compound="center", fg="#00FF00", bd=-4)
upload_label.grid(row=3, column=2)
l7 = Label(root, font=("Orbitron", 20, "bold"),bg="black", fg="#00FF00" , text="Upload Speed")
l7.grid(row=4, column=2)

ping_label = Label(root, font=("Orbitron", 30, "bold"), text="0 ms", image=tk_image, compound="center", fg="#00FF00", bd=-4)
ping_label.grid(row=3, column=3)
l8 = Label(root,  font=("Orbitron", 20, "bold"),bg="black", fg="#00FF00" ,text="Ping")
l8.grid(row=4, column=3)

usage()
root.mainloop()


