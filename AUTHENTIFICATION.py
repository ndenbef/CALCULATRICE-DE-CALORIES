import tkinter as tk

window = tk.Tk()
window.title("CALCULATRICE DE CALORIES")
#window.geometry("1320x820")
window.geometry("1080x400")
window.configure(bg="#0E4F77")

frame1 = tk.Frame(window, bg="#0E4F77")

label0 = tk.Label(frame1, text = "CALCULATRICE DE CALORIES", font=("helvetica", 30), fg="white", bg="#0E4F77", pady=40)
label0.grid(row=0, column=0, columnspan=3)

label0 = tk.Label(frame1, text = "Connexion", font=("helvetica", 20), fg="white", bg="#0E4F77")
label0.grid(row=1, column=1)

Label1 = tk.Label(frame1, text="UserName ", font=("helvetica", 20), bg="#0E4F77", pady=20, padx=3) 
Label1.grid(row=2, column=0, sticky="w")

Entry1 = tk.Entry(frame1, text="      ", font=("helvetica", 20))
Entry1.grid(row=2, column=1, columnspan=2)

Label2 = tk.Label(frame1, text=" Password ", font=("helvetica", 20), bg="#0E4F77", pady=20) 
Label2.grid(row=3, column=0, sticky="w")

Entry2 = tk.Entry(frame1, text="      ", show="*", font=("helvetica", 20))
Entry2.grid(row=3, column=1, columnspan=2)

Login = tk.Button(frame1, text="LOGIN", font=("helvetica", 15), fg="white", bg="#0E4F77", pady=10)
Login.grid(row=4, column=2, sticky="e")

Create = tk.Button(frame1, text="I don't have an Account", font=("helvetica", 10), fg="white", bg="#0E4F77", relief="flat", pady=10)
Create.grid(row=4, column=1, sticky="w")

frame1.pack(anchor="center")

window.mainloop()