import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

history = []

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_tosses(n):
    heads_count = 0
    tails_count = 0

    for _ in range(n):
        result = coin_toss()
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    history.append((n, heads_count, tails_count))
    return heads_count, tails_count

def flip_coin():
    try:
        flips = int(entry.get())
        if flips <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive number.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return
    heads, tails = multiple_tosses(flips)
    heads_label.config(text=f"Heads: {heads} ({(heads/flips)*100:.2f}%)")
    tails_label.config(text=f"Tails: {tails} ({(tails/flips)*100:.2f}%)")
    last_result = "Heads" if random.random() < (heads / flips) else "Tails"
    coin_image_label.config(image=heads_img if last_result == "Heads" else tails_img)

def show_history():
    if not history:
        messagebox.showinfo("History", "No coin flips recorded yet!")
        return

    history_text = "Previous Sessions:\n"
    for i, (flips, heads, tails) in enumerate(history, 1):
        history_text += f"Session {i}: {flips} flips -> Heads: {heads}, Tails: {tails}\n"
    
    messagebox.showinfo("History", history_text)

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Virtual Coin Toss")
root.geometry("400x500")

heads_img_raw = Image.open("heads.png").resize((150, 150))
tails_img_raw = Image.open("tails.png").resize((150, 150))
heads_img = ImageTk.PhotoImage(heads_img_raw)
tails_img = ImageTk.PhotoImage(tails_img_raw)

title_label = tk.Label(root, text="Virtual Coin Toss", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter the number of flips:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack(pady=5)

flip_button = tk.Button(root, text="Flip Coin", command=flip_coin)
flip_button.pack(pady=10)

heads_label = tk.Label(root, text="Heads: 0 (0.00%)")
heads_label.pack()
tails_label = tk.Label(root, text="Tails: 0 (0.00%)")
tails_label.pack()

coin_image_label = tk.Label(root, image=heads_img)
coin_image_label.pack(pady=10)

history_button = tk.Button(root, text="View History", command=show_history)
history_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack(pady=10)

root.mainloop()
