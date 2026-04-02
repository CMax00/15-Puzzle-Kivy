import kivy

kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

blocks = []
empty = (0, 0)
gridSize = 4
layout = GridLayout(cols=gridSize, rows=gridSize, spacing=10, padding=20)


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

        for x in range(-1, 2):
            for y in range(-1, 2):
                # excludes the block in diagonal
                if abs(x) + abs(y) != 2:
                    # tests if that po is empty
                    if self.x + x == empty[0] and self.y + y == empty[1]:
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
                x = i % 4
                y = i // 4

                # creates block and adds it to the layout
                block = Block(x, y, i + 1)
                layout.add_widget(block.button)
                blocks.append(block)
            else:
                x = i % 4
                y = i // 4
                empty = (x, y)
                block = Block(x, y, 0)
                layout.add_widget(block.button)
                blocks.append(block)

        return layout


if __name__ == '__main__':
    MyApp().run()
