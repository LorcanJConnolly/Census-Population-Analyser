import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from dist_test.py import Population_Dist_Tester

class Animation:
    def __init__(self):
        self.PDT = Population_Dist_Tester()
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])
        self.xdata = []
        self.ydata = []


    def init(self):
        self.line.set_data([], [])
        return self.line, 


    def update(self, frame):
        self.func(frame)
        self.line.set_data(self.xdata, self.ydata)  # Update values
        self.ax.set_xlim(0, max(self.xdata) + 1)
        self.ax.set_ylim(0, max(self.ydata) + 1)
        self.fig.canvas.draw()  # update the canvas so the axes update
        return self.line,


    def run(self):
        ani = FuncAnimation(
            self.fig,
            self.update,
            frames=range(20), 
            init_func=self.init, 
            blit=True, 
            repeat=False
        )
        plt.show()

if __name__ == "__main__":
    obj = Animation()
    obj.run()
