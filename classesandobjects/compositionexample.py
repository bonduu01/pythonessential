import time


class Tracks:
    @staticmethod
    def change_direction(left, on):
        print("tracks: ", left, on)


class Wheels:
    @staticmethod
    def change_direction(left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)
