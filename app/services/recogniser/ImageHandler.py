import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from Recogniser import recognise_factory


class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        file = str(event.src_path)
        if file.endswith('.jpg') and 'output.png' not in file:
            print(f"Image Recieved: {file}")
            time.sleep(2)
            recognise_factory(file)


observer = Observer()
event_handler = ImageHandler()
observer.schedule(event_handler, path='./')
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
