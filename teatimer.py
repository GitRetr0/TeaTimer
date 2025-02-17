import tkinter as tk
from tkinter import ttk

#definition for some info about types of tea and general recommendations for infusing

tea_info = {
    "Most black tea" :{
        "boiling_temp": 100,
        "infusing_time_range": "3-5 minutes",
        "default_time": 180 #lower bound (3 minutes)
    },
    "Green tea" :{
        "boiling_temp": 80,
        "infusing_time_range": "2-3 minutes",
        "default_time": 120 #lower bound (2 minutes)
    
    }
    
}
def update_info(*args):
    #update the recommended info and time entry based on tea selection
    selected = tea_var.get()
    info = tea_info[selected]
    recommended_label.config(text=f"Recommended infusing time: {info['infusing_time_range']}")
    boiling_label.config(text=f"Boiling temperature: {info['boiling_temp']}°C")
    
    #update timer entry
    timer_entry.delete(0, tk.END)
    timer_entry.insert(0, str(info["default_time"]))
    
def start_timer():
    #start the countdown timer
    try: 
        total_seconds = int(timer_entry.get())
    except ValueError:
        time_label.config(text="Please, enter a valid number!")
        return
    countdown(total_seconds)
    
def countdown(count):
    #countdown func that updates the timer label every second
    minutes = count // 60
    seconds = count % 60
    time_label.config(text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        #call this func after 1000 ms (1 sec)
        root.after(1000, countdown, count - 1)
    else:
        time_label.config(text="Tea is ready!")
        
#Main window

root= tk.Tk()
root.title("Tea Timer")

#Frame for padding

frame = ttk.Frame(root, padding=20)
frame.pack()

#Tea type selection dropdown
tk.Label(frame, text="Select your tea type:").grid(row=0, column=0, sticky="w")
tea_var = tk.StringVar(frame)
tea_var.set("Most black tea") #default selection
tea_menu = ttk.OptionMenu(frame, tea_var, tea_var.get(), *tea_info.keys(), command=update_info)
tea_menu.grid(row=0, column=1, pady=5)

recommended_label = ttk.Label(frame, text="")
recommended_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=2)
boiling_label = ttk.Label(frame, text="")
boiling_label.grid(row=2, column=0, columnspan=2, sticky="w",pady=2)

tk.Label(frame, text="Set Timer (seconds):").grid(row=3, column=0, sticky="w", pady=2)
timer_entry = ttk.Entry(frame, width=10)
timer_entry.grid(row=3, column=1, sticky="w", pady=5)

start_button = ttk.Button(frame, text="Start Timer", command=start_timer)
start_button.grid(row=4, column=0, columnspan=2, pady=10)
time_label = ttk.Label(frame, text="00:00", font=("Helvetica", 24))
time_label.grid(row=5, column=0, columnspan=2, pady=10)

update_info()
root.mainloop()