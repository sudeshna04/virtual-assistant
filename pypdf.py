import PyPDF2
import tkinter as tk
from tkinter import filedialog
import pyttsx3
import threading

# Initialize text-to-speech engine
engine = pyttsx3.init()

def read_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def open_and_read_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        text = read_pdf(file_path)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)
        # Use a thread to avoid freezing the GUI
        threading.Thread(target=speak_text, args=(text,), daemon=True).start()

# GUI setup
root = tk.Tk()
root.title("PDF Reader with Voice (PyPDF2)")

open_button = tk.Button(root, text="Open PDF", command=open_and_read_pdf)
open_button.pack(pady=10)

text_box = tk.Text(root, wrap="word", width=100, height=30)
text_box.pack(padx=10, pady=10)

root.mainloop()
