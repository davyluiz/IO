import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

folder_path = '' # Diretório de escuta

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None
        else:
            # Quando um arquivo é adicionado
            file_path = event.src_path
            print(f"Novo arquivo detectado: {file_path}")

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
