import tkinter as tk
import pyautogui
import time
import threading

def start_typing():
    def type_text():
        time.sleep(2)  # Give user 3 seconds to focus the typing field
        user_input = text_box.get("1.0", tk.END).strip()
        pyautogui.write(user_input, interval=0.01)  # Fast typing with 10ms delay
    threading.Thread(target=type_text).start()

# GUI Setup
root = tk.Tk()
root.title("Baller")

tk.Label(root, text="Enter text to auto type:").pack(pady=5)

text_box = tk.Text(root, height=5, width=40)
text_box.pack(pady=5)

start_button = tk.Button(root, text="Start Typing (after 3s)", command=start_typing)
start_button.pack(pady=10)

root.mainloop()
