
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):

    xs = []
    ys = []

    
    data = open("PINGINFO.txt", "r").read()
    lines = data.split("\n")
    for line in lines:
        if len(line) > 1:
            line = line.split(",")
            xs.append(line[0])
            ys.append(float(line[1]))


    ax1.clear()
    plt.xlabel('Time')
    plt.ylabel('Ping')
    plt.xticks(rotation=70)
    ax1.plot(xs,ys,'-o')
    

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
