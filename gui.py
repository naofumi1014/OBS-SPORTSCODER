import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import json


# tkinter
root = tk.Tk()
root.title(u"得点送出GUI")
root.geometry("800x450")

#file_path
file_path = 'point_data\\point.json'

with open(file_path, 'r', encoding="utf-8_sig") as f:
    json_data = json.load(f)

#HOME
home = tk.Label(root, text="HOME", font=("Arial", 25))
hometeam = tk.Label(root, text="TEAM", font=("Arial", 25))
homepoint = tk.Label(root, text="POINT", font=("Arial", 25))

home.place(x=50,y=50)
hometeam.place(x=50,y=100)
homepoint.place(x=50,y=150)

hometeam_entry = tk.Entry(root,                     
                    font=("Arial", 15),
                    width=15,
                    justify="center")

homepoint_entry = tk.Entry(root,                     
                    font=("Arial", 25),
                    width=3,
                    justify="center",
                    )
hometeam_entry.insert(0,json_data["HOME"]["team"])
homepoint_entry.insert(0,str(json_data["VISITOR"]["point"]))

hometeam_entry.place(x=160,y=110)
homepoint_entry.place(x=230,y=150)
#VISITOR

visitor = tk.Label(root, text="VISITOR", font=("Arial", 25))
visitorteam = tk.Label(root, text="TEAM", font=("Arial", 25))
visitorpoint = tk.Label(root, text="POINT", font=("Arial", 25))

visitor.place(x=570,y=50)
visitorteam.place(x=600,y=100)
visitorpoint.place(x=600,y=150)

visitorteam_entry = tk.Entry(root,                     
                    font=("Arial", 15),
                    width=15,
                    justify="center")

visitorpoint_entry = tk.Entry(root,                     
                    font=("Arial", 25),
                    width=3,
                    justify="center")

visitorteam_entry.insert(0,json_data["VISITOR"]["team"])
visitorpoint_entry.insert(0,str(json_data["VISITOR"]["point"]))

visitorteam_entry.place(x=420,y=110)
visitorpoint_entry.place(x=480,y=150)

#PERIOD
period = tk.Label(root, text="PERIOD", font=("Arial", 25))
period.place(x=250, y=250)
period_option = ["1st", "2nd", "3rd", "Ex","GWS","前半","後半","延前","延後"]  # 選択肢 #game winning showt:サッカーのＰＫみたいなやつ
variable = tk.StringVar()
period_combo = ttk.Combobox(root, values=period_option,
                             textvariable=variable,
                             font=("Arial", 25),
                             width=4,
                             state="readonly",
                             justify="center")
period_combo.current(0)
period_combo.place(x=400, y=250)

#送出
register_button = tk.Button(root, text="送出",font=("Arial", 25))
register_button.place(x=330, y=330)

class function():
    def send_out(self):
        
        file_path = r'point_data\\point.json'
        with open(file_path, 'r', encoding="utf-8_sig") as f:
            json_data = json.load(f)
            
        hometeam = hometeam_entry.get()
        homepoint = int(homepoint_entry.get())
        visitorteam = visitorteam_entry.get()
        visitorpoint = int(visitorpoint_entry.get())
        period = period_combo.get()
        
        json_data["HOME"]["team"] = hometeam
        json_data["HOME"]["point"] = homepoint
        json_data["VISITOR"]["team"] = visitorteam
        json_data["VISITOR"]["point"] = visitorpoint   
        json_data["PERIOD"] = period  
        
        print(hometeam,homepoint,visitorteam,visitorpoint,period)
        
        with open(file_path, mode='w', encoding="utf-8_sig") as f:
            json.dump(json_data, f, ensure_ascii=False)

functionclass = function()
register_button["command"] = functionclass.send_out
        
# main loop
root.mainloop()