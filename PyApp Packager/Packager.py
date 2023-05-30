# OS routines for NT or Posix
import os
# Wrapper functions for Tcl/Tk.
import tkinter as tk
# File selection dialog classes from the Wrapper functions for Tcl/Tk.
from tkinter import filedialog
# Read and write ZIP files.
import zipfile


def create_pyapp_archive(source_dir, target_file):
    # Create a new ZIP archive
    with zipfile.ZipFile(target_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Check if the source directory is a file
        if os.path.isfile(source_dir):
            # Add the single file to the archive with the folder path
            zipf.write(source_dir, os.path.basename(source_dir))
        else:
            # Iterate through all files and directories in the source directory
            for root, _, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Get the relative path of the file from the source directory
                    relative_path = os.path.relpath(file_path, source_dir)
                    # Add each file to the archive using the updated file path
                    zipf.write(file_path, os.path.join('program_files', relative_path))


# Create Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Ask user to select source directory using a file dialog
source_directory = filedialog.askdirectory(title="Select Source Directory")

if source_directory:
    # Ask user to select target archive file using a file dialog
    target_archive = filedialog.asksaveasfilename(
        defaultextension=".pyapp",
        filetypes=[("PyApp Archive", "*.pyapp")],
        title="Save PyApp Archive"
    )

    if target_archive:
        create_pyapp_archive(source_directory, target_archive)
        print("PyApp archive created successfully!")

    else:
        print("Target archive file not selected.")

else:
    print("Source directory not selected.")
