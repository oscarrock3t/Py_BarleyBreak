import tkinter, random

"""Сделать: 2 экрана - задание, решение; Сделано: рандомная закраска, все цвета в 1"""

class BarleyBreak(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=320, height=320)
        self.colors = ['#4BA8C1', '#C1634B']
        self.field = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.bind('<Button-1>', self.change_values)

    def create_quest(self):
        for i in range(2):
            for j in range(2):
                self.field[i][j] = random.choice([0, 1])
        print(self.field)

    def draw_elements(self):
        """y - i, x - j"""
        rect_size = 100
        for i_idx, i_value in enumerate(self.field):
            for j_idx, j_value in enumerate(i_value):
                x1 = j_idx * rect_size
                y1 = i_idx * rect_size
                x2 = x1 + rect_size
                y2 = y1 + rect_size
                self.create_rectangle(x1, y1, x2, y2, fill=self.colors[j_value], outline='black')

    def change_values(self, event):
        i = event.y // 100
        j = event.x // 100
        coups = [[i, j],
                 [i - 1, j],
                 [i, j + 1],
                 [i + 1, j],
                 [i, j - 1]]
        for i, j in coups:
            if i < 0 or j < 0 or i > 2 or j > 2:
                continue
            else:
                self.field[i][j] = not self.field[i][j]
        self.draw_elements()
        self.check_result()

    def check_result(self):
        end = 0
        for i in self.field:
            end += sum(i)
        if end == 0 or end == 9:
            print('YOU\'RE WINNER!')
            self.quit()

def main():
    window = tkinter.Tk()
    game = BarleyBreak(window)
    game.create_quest()
    game.draw_elements()
    game.pack()
    window.mainloop()


if __name__ == '__main__':
    main()
