from threading import Event, Semaphore, Thread


class Controller:
    def __init__(self, model, view):
        self.event = Event()
        self.semaphore = Semaphore()
        self.model = model
        self.view = view

    def new_timer(self, time, use_semaphore=False):
        if self.event.is_set():
            self.event.clear()
        thread = Thread(target=self.__create_timer, args=(time, use_semaphore))
        thread.start()

    def __create_timer(self, time, use_semaphore):
        if not use_semaphore:
            self.model.timer(time, self.event)
        else:
            try:
                self.semaphore.acquire()
                self.model.timer(time, self.event)
            finally:
                self.semaphore.release()

    def stop(self):
        self.event.set()
