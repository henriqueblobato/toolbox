'''
Created on 24 de jul de 2017

@author: henrique

Usage: python watchdog_model.py <path>


'''


import sys, os.path, time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyEventHandler(PatternMatchingEventHandler):
    def on_moved(self, event):
        print("File %s was just moved to %s" %(event.src_path, event.dest_path))

    def on_created(self, event):
        print("File %s was just created" % event.src_path)

    def on_deleted(self, event):
        print("File %s was just deleted" % event.src_path)

    def on_modified(self, event):
        print("File %s was just modified" % event.src_path)

def main(file_path=None):
    watched_dir = os.path.split(file_path)[0]
    print('watched_dir = {watched_dir}'.format(watched_dir=watched_dir))
    patterns = [file_path]
    print('patterns = {patterns}'.format(patterns=', '.join(patterns)))
    event_handler = MyEventHandler(patterns=patterns)
    observer = Observer()
    observer.schedule(event_handler, watched_dir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



if __name__ == "__main__":
#     uncomment for an specific path
#     main(file_path=os.getcwd()) 

    if len(sys.argv) > 1:
        path = sys.argv[1]
        main(file_path=path.strip())
    else:
        sys.exit(1)
