import os
import tkinter as tk
from tkinter import filedialog
import zipfile

def open_pyapp(pyapp_file):
    if pyapp_file.endswith('.pyapp'):
        extract_path = 'Python Application Manager/runtime_files'  # Specify the extract path here
        with zipfile.ZipFile(pyapp_file, 'r') as zipf:
            zipf.extractall(path=extract_path)
        print(f"Successfully opened PyApp archive: {pyapp_file}")
    else:
        print(f"Error: {pyapp_file} is not a valid PyApp archive.")

# Create Tkinter window
root = tk.Tk()
root.withdraw()

# Ask the user to select a PyApp archive using a file dialog
pyapp_file = filedialog.askopenfilename(
    filetypes=[("PyApp Archive", "*.pyapp")],
    title="Open PyApp Archive"
)

if pyapp_file:
    open_pyapp(pyapp_file)
else:
    print("No PyApp archive selected.")

input("press enter to close ")