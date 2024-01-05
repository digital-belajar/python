from ship import Ship


class ShipTurbo(Ship):
    def move_up(self):
        self.y -= 10

    def move_down(self):
        self.y += 10