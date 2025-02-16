import tkinter as tk
from tkinter import scrolledtext
import prompts

def show_popup(summary_text):
  root = tk.Tk()
  root.title("Video Analysis Result")

  # Set the window size to be larger
  root.geometry("800x600")

  # Create a frame for better layout management
  frame = tk.Frame(root, bg="lightblue")
  frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

  # Create a scrolled text area with a larger size
  text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=("Arial", 12), bg="white", fg="black")
  text_area.insert(tk.INSERT, summary_text)
  text_area.config(state="disabled")
  text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

  # Add a close button
  close_button = tk.Button(frame, text="Close", command=root.destroy, bg="red", fg="white", font=("Arial", 10, "bold"))
  close_button.pack(pady=10)

  root.mainloop()



#Tests:
# summary = prompts.placeholderText
# show_popup(summary)