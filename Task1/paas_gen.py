import tkinter as tk
import random,string

def generate_password():
    pwd_len = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(pwd_len))
    password_label.config(text="Generated Password : " + password)

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("380x220")
root.iconbitmap(r"C:\Users\rituh\OneDrive\Desktop\python projects\codsoft\Codsoft\Task1\reset_password_EwT_icon.ico")
root.resizable(False, False)
root.configure(bg="#FAEBD7")

label=tk.Label(root,text='password Generator',font='Consolas 25 bold',padx=20,pady=10, width=20,bg='#66CDAA',fg='black')
label.pack()
length_label = tk.Label(root, text="Password Length:",font='Consolas 15 bold',padx=20,pady=10,bg="#FAEBD7",width=20,fg='black')
length_label.pack()
length_entry = tk.Entry(root,font='times 15')
length_entry.pack()
generate_button = tk.Button(root,text='Generate Password',font='times 13 bold',bg='#9ACD32',command=generate_password)
generate_button.pack()
password_label = tk.Label(root, text="Generated Password: ",font='Consolas 11 bold',bg="#FAEBD7",width=60,fg='black')
password_label.pack()
root.mainloop()

                          
