import tkinter as tk
from datetime import datetime


def update_clock() -> None:
	current_time = datetime.now().strftime("%H:%M:%S")
	time_label.config(text=current_time)
	date_label.config(text=datetime.now().strftime("%A, %B %d, %Y"))
	root.after(1000, update_clock)


root = tk.Tk()
root.title("Digital Clock")
root.geometry("420x200")
root.resizable(False, False)
root.configure(bg="#101820")

time_label = tk.Label(
	root,
	font=("Segoe UI", 48, "bold"),
	fg="#F2AA4C",
	bg="#101820",
)
time_label.pack(pady=(32, 4))

date_label = tk.Label(
	root,
	font=("Segoe UI", 14),
	fg="#F2F2F2",
	bg="#101820",
)
date_label.pack()

update_clock()
root.mainloop()