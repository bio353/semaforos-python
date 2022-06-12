from playsound import playsound as play


class Model:
    def __init__(self):
        self.counter = 0

    def timer(self, time, event):
        self.counter += 1
        id = self.counter
        finished = False
        while not event.is_set() and not finished:
            print(f'Alarm {id}: {time}min left...\n')
            event.wait(INTERVAL)
            time -= 1
            finished = True if time == 0 else False
        if finished:
            print(f'Alarm {id} finished!\n')
            play('assets/zapzap.mp3')
        else:
            print(f'Alarm {id} interrupted!\n')


INTERVAL = 6  # in seconds
