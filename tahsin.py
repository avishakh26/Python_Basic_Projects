


import tkinter as tk
from tkinter import filedialog, messagebox



# Function to save the file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(text_area.get(1.0, tk.END))
            messagebox.showinfo("Save File", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {e}")

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if file_path:
        try:
            with open(file_path, 'r') as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", f"Error opening file: {e}")

# Function to clear the text area
def clear_text():
    text_area.delete(1.0, tk.END)

# Setting up the main window
root = tk.Tk()
root.title("Simple Notepad")
root.geometry("600x400")

# Text area for writing
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

# Menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Clear", command=clear_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Configuring the menu bar
root.config(menu=menu_bar)

# Start the application
root.mainloop()
