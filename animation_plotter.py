import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Animation:
    def __init__(self, xdata, ydata):
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])
        self.xdata = xdata
        self.ydata = ydata

    def init(self):
        self.line.set_data([], [])
        self.ax.set_xlim(self.xdata[0]+self.xdata[0]//10, -self.xdata[0]//20)
        self.ax.set_ylim(0, max(self.ydata)+0.1)
        return self.line, 

    def update(self, frame):
        self.line.set_data(self.xdata[:frame], self.ydata[:frame])  
        self.fig.canvas.draw()
        return self.line,

    def run(self):
        ani = FuncAnimation(
            self.fig,
            self.update,
            frames=range(len(self.xdata)+1), 
            init_func=self.init, 
            blit=True, 
            repeat=False
        )
        plt.show()


