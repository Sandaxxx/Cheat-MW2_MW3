import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("340x600")
app.title("Cheat Sandax")

def cheater_notif():
    ctk.messagebox.showinfo(f"Alert", "stop trying to cheat big shit...")

frame_1 = ctk.CTkFrame(master=app)

frame_1.pack(pady=30, padx=30, fill="both", expand=True)

label_1 = ctk.CTkLabel(master=frame_1, text="FOV (0-200)")
label_1.pack(pady=5, padx=5)

slider_1 = ctk.CTkSlider(master=frame_1, from_=0, to=1)
slider_1.pack(pady=5, padx=5)
slider_1.set(0.5)

checkbox_1 = ctk.CTkCheckBox(master=frame_1, text="Aimbot", command=cheater_notif)
checkbox_1.pack(pady=10, padx=10)

checkbox_2 = ctk.CTkCheckBox(master=frame_1, text="Wallhack", command=cheater_notif)
checkbox_2.pack(pady=10, padx=10)

checkbox_3 = ctk.CTkCheckBox(master=frame_1, text="UAV+", command=cheater_notif)
checkbox_3.pack(pady=10, padx=10)

switch_1 = ctk.CTkSwitch(master=frame_1, text="[+] Unlimited Slide", command=cheater_notif)
switch_1.pack(pady=10, padx=10)

switch_5 = ctk.CTkSwitch(master=frame_1, text="[+] Unlimited Ammo", command=cheater_notif)
switch_5.pack(pady=10, padx=10)

optionmenu_1 = ctk.CTkOptionMenu(frame_1, values=["Diamond", "Gold", "Atomic"])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("Swap CAMO")

bouton1 = ctk.CTkButton(frame_1, text="[+] Unlock all", command=cheater_notif)
bouton1.pack(pady=15, padx=10)

bouton2 = ctk.CTkButton(frame_1, text="[+] Off Anti-Cheat", command=cheater_notif)
bouton2.pack(pady=15, padx=10)

bouton3 = ctk.CTkButton(frame_1, text="[+] Spoof Account", command=cheater_notif)
bouton3.pack(pady=15, padx=10)


app.mainloop()
