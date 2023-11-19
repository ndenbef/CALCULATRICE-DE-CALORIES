import tkinter as tk

window = tk.Tk()
window.title("CALCULATRICE DE CALORIES")
window.geometry("1400x750")
#window.geometry("1080x400")
window.configure(bg="#0E4F77")

frame1 = tk.Frame(window, bg="#0E4F77")

Label2 = tk.Label(frame1, text="", font=("helvetica", 20), bg="#0E4F77", pady=80) 
Label2.grid(row=0, column=0, sticky="w")

save = tk.Button(frame1, text="ENREGISTREMENT    ", font=("helvetica", 10), fg="white", bg="#0E4F77", pady=20)
save.grid(row=1, column=0, sticky="w")

Label2 = tk.Label(frame1, text="", font=("helvetica", 20), bg="#0E4F77", pady=5) 
Label2.grid(row=2, column=0, sticky="w")

graph = tk.Button(frame1, text="VOIR MON GRAPHIQUE", font=("helvetica", 10), fg="white", bg="#0E4F77", pady=20)
graph.grid(row=3, column=0, sticky="w")

Label2 = tk.Label(frame1, text="", font=("helvetica", 20), bg="#0E4F77", pady=5) 
Label2.grid(row=4, column=0, sticky="w")

export = tk.Button(frame1, text="TELECHARGEMENT    ", font=("helvetica", 10), fg="white", bg="#0E4F77", pady=20)
export.grid(row=5, column=0, sticky="w")

Label2 = tk.Label(frame1, text="", font=("helvetica", 20), bg="#0E4F77", pady=30) 
Label2.grid(row=6, column=0, sticky="w")

logout = tk.Button(frame1, text="DECONNEXION", font=("helvetica", 15), fg="red", bg="#0E4F77", pady=30, relief="flat")
logout.grid(row=7, column=0, sticky=tk.S+tk.W)



frame1.pack(anchor="w")

window.mainloop()