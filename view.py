import tkinter as tk
from tkinter.filedialog import asksaveasfile

def save_file(formatted_filename, file_data, audio_extension):
    window = tk.Tk()
    window.wm_attributes('-topmost', 1)
    window.withdraw()
    f = asksaveasfile(mode='wb', initialfile=formatted_filename,
                    defaultextension=audio_extension, parent=window,
                    filetypes=[('All types(*.*)', '*.*')])
    f.write(file_data)
    f.close()