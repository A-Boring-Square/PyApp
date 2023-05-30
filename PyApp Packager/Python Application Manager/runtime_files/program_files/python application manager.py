import os
import tkinter as tk
from tkinter import filedialog
import zipfile

def open_pyapp(pyapp_file):
    if pyapp_file.endswith('.pyapp'):
        with zipfile.ZipFile(pyapp_file, 'r') as zipf:
            # Extract the contents of the ZIP file
            zipf.extractall('program_files')
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

# Add your additional code or actions here




def generate_buttons(directory):
    # Clear existing buttons
    for button in button_frame.winfo_children():
        button.destroy()

    # Find .pyapp files in the directory
    pyapp_files = [file for file in os.listdir(directory) if file.endswith(".pyapp")]

    # Generate buttons for each .pyapp file
    for pyapp_file in pyapp_files:
        button = tk.Button(button_frame, text=pyapp_file, command=lambda file=pyapp_file: open_pyapp(file))
        button.pack()

# Create Tkinter window
root = tk.Tk()
root.geometry('500x500')
root.title("Python Application Manager")

def select_directory():
    directory = filedialog.askdirectory(title="Select Directory")
    if directory:
        generate_buttons(directory)

# Create a button to select the directory
select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack()

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack()

root.mainloop()

