import tkinter as tk
from tkinter import scrolledtext
import prompts

def show_popup(summary_text):
  root = tk.Tk()
  root.title("Video Analysis Result")

  text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
  text_area.insert(tk.INSERT, summary_text)
  text_area.config(state="disabled")
  text_area.pack(padx=10, pady=10)

  root.mainloop()

# summary = prompts.placeholderText


# show_popup(summary)