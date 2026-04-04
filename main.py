import kivy
import random

kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock

blocks = []
empty = (0, 0)
oldEmpty = (-10, -10)
gridSize = 4
mixSteps = 500
timeBetweenMixSteps = 0
layout = GridLayout(cols=gridSize, rows=gridSize, spacing=10, padding=20)


def mixGrid():
    x, y = 0, 0
    # Generates random move until it is valid
    while (x + y == 0  # prevents no movement
           or empty[0] + x < 0 or empty[0] + x > gridSize - 1  # prevents impossible move
           or empty[1] + y < 0 or empty[1] + y > gridSize - 1
           or oldEmpty == (empty[0] + x, empty[1] + y)):  # prevents undoing last move
        # Makes a random move
        x = random.randrange(-1, 2)
        y = random.randrange(-1, 2)

    # Finds the selected block to move
    for block in blocks:
        if (block.x, block.y) == (empty[0] + x, empty[1] + y):
            block.move(None)
            break


def mixStep(dt):
    global mixSteps
    # Stops when no steps remain
    if mixSteps <= 0:
        return False

    mixGrid()
    mixSteps -= 1


# puts the blocks into the grid according to their pos
def reloadGrid():
    layout.clear_widgets()
    # converts the pos into an int for sorting
    blocks.sort(key=lambda block: block.x + gridSize * block.y)

    for block in blocks:
        layout.add_widget(block.button)


class Block:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
        self.button = Button(text=str(self.number), font_size=32)
        self.button.bind(on_press=self.move)
        self.button.background_down = self.button.background_normal

        # makes the empty button seem empty
        if self.number == 0:
            self.button.opacity = 0
            self.button.disabled = True

    # switches block with empty if it is next to it
    def move(self, instance):
        global empty
        global oldEmpty

        for x in range(-1, 2):
            for y in range(-1, 2):
                # excludes the block in diagonal
                if abs(x) + abs(y) != 2:
                    # tests if that po is empty
                    if self.x + x == empty[0] and self.y + y == empty[1]:
                        oldEmpty = empty
                        empty = (self.x, self.y)
                        self.x, self.y = self.x + x, self.y + y

                        for block in blocks:
                            if block.number == 0:
                                block.x, block.y = empty[0], empty[1]

                        reloadGrid()
                        return


class MyApp(App):

    def build(self):
        global empty

        # total amount of blocks
        for i in range(gridSize ** 2):
            # leaves one space for the empty block
            if i <= (gridSize ** 2) - 2:
                # converts number into x, y pos
                x = i % gridSize
                y = i // gridSize

                # creates block and adds it to the layout
                block = Block(x, y, i + 1)
                layout.add_widget(block.button)
                blocks.append(block)
            else:
                x = i % gridSize
                y = i // gridSize
                empty = (x, y)
                block = Block(x, y, 0)
                layout.add_widget(block.button)
                blocks.append(block)

        return layout

    def on_start(self):
        # Run the mixSteps
        # This method is used so the screen updates between the Steps
        Clock.schedule_interval(mixStep, timeBetweenMixSteps)


if __name__ == '__main__':
    MyApp().run()
