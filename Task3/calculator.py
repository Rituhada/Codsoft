import tkinter as tk

def btn_click(event):
    current_text = result_label.cget("text")
    button_text = event.widget.cget("text")
    
    if button_text == "=":
        try:
            result = eval(current_text)
            result_label.config(text=result)
        except Exception as e:
            result_label.config(text="Error")
    elif button_text == "C":
        result_label.config(text="")
    elif button_text == "X":
        result_label.config(text="")
    elif button_text == "%":
        result_label.config(text=str(eval(current_text) / 100))
    else:
        result_label.config(text=current_text + button_text)

def toggle_calculator():
    if calculator_frame.winfo_ismapped():
        calculator_frame.grid_forget()
        on_off_button.config(text="ON", bg="#FF5722")
    else:
        calculator_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        on_off_button.config(text="OFF", bg="#FFA726")

root = tk.Tk()
root.title("Calculator")
root.iconbitmap(r"C:\Users\rituh\OneDrive\Desktop\python projects\codsoft\Codsoft\Task3\calculator_J0j_icon (1).ico")
root.configure(bg="white")

result_label = tk.Label(root, text="", font=("Calibri", 20), anchor="e", bg="white", fg="black")
result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

calculator_frame = tk.Frame(root, bg="#E5E5E5")

button_labels = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "X", "%", "00"
]
row = 0
col = 0
for label in button_labels:
    button = tk.Button(calculator_frame, text=label, font=("Calibri", 15), padx=20, pady=20, bg="white", fg="black", relief="flat")
    if label in ["+", "-", "*", "%", "=","00","/","X",".","C"]:
        button.configure(fg="black")
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", btn_click)  
    col += 1
    if col > 3:
        col = 0
        row += 1

on_off_button = tk.Button(root, text="ON", font=("Calibri", 12), padx=10, pady=5, bg="#FF5722", fg="white", relief="flat", command=toggle_calculator)
on_off_button.grid(row=2, column=0, columnspan=4, pady=5)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
