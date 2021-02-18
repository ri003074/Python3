from pynput import mouse


class Monitor:
    def __init__(self):
        self.counter = 0
        self.over_count = 5

    def count(self):
        self.counter += 1
        print(f"Count: {self.counter}")

    def is_over(self):
        return True if self.counter >= self.over_count else False

    def call(self):
        self.count()
        if self.is_over():
            print("Done")
            self.listner.stop()

    def on_click(self, x, y, button, pressed):
        if pressed:
            print(f"{x,y} pressed")
            self.call()

    def start(self):
        with mouse.Listener(on_click=self.on_click) as self.listner:
            self.listner.join()


monitor = Monitor()
monitor.start()
