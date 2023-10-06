import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("340x600")
app.title("Cheat Sandax")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=30, padx=30, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="FOV (0-200)")
label_1.pack(pady=5, padx=5)


slider_1 = customtkinter.CTkSlider(master=frame_1, from_=0, to=1)
slider_1.pack(pady=5, padx=5)
slider_1.set(0.5)


checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text="Aimbot")
checkbox_1.pack(pady=10, padx=10)

checkbox_2 = customtkinter.CTkCheckBox(master=frame_1, text="Wallhack")
checkbox_2.pack(pady=10, padx=10)

checkbox_3 = customtkinter.CTkCheckBox(master=frame_1, text="UAV+")
checkbox_3.pack(pady=10, padx=10)


switch_1 = customtkinter.CTkSwitch(master=frame_1, text="[+] Unlimited Slide")
switch_1.pack(pady=10, padx=10)
switch_5 = customtkinter.CTkSwitch(master=frame_1, text="[+] Unlimited Ammo")
switch_5.pack(pady=10, padx=10)


optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Diamond", "Gold", "Atomic"])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("Swap CAMO")

bouton1 = customtkinter.CTkButton(frame_1, text="[+]  Unlock all")
bouton1.pack(pady=15, padx=10)

bouton2 = customtkinter.CTkButton(frame_1, text="[+]  Off Anti-Cheat")
bouton2.pack(pady=15, padx=10)

bouton2 = customtkinter.CTkButton(frame_1, text="[+]  Spoof Account")
bouton2.pack(pady=15, padx=10)



app.mainloop()