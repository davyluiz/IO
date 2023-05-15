import time
import tkinter as tk
from tkinter import filedialog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def on_created(self, event):
        if event.is_directory:
            return None
        else:
            # Quando um arquivo é adicionado
            file_path = event.src_path
            message = f"Novo arquivo detectado: {file_path}\n"
            self.text_widget.insert(tk.END, message)


def start_observer(folder_path, text_widget):
    event_handler = MyHandler(text_widget)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


def select_folder(text_widget):
    folder_path = filedialog.askdirectory()
    if folder_path:
        text_widget.delete(1.0, tk.END)
        start_observer(folder_path, text_widget)


root = tk.Tk()
root.title("Observador de diretórios")

# Widget de texto para exibir mensagens
text_widget = tk.Text(root, height=10, width=50)
text_widget.pack(padx=10, pady=10)

# Botão para selecionar a pasta a ser observada
select_folder_button = tk.Button(root, text="Selecionar diretório", command=lambda: select_folder(text_widget))
select_folder_button.pack(padx=10, pady=10)

# Botão para sair do programa
quit_button = tk.Button(root, text="Sair", command=root.quit)
quit_button.pack(padx=10, pady=10)

root.mainloop()
