
import mplcursors
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates

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
            line[0] = mdates.datestr2num(line[0])
            xs.append(line[0])
            
            ys.append(float(line[1]))

            ax1.clear()
            plt.xlabel('Timeline (H:M:S)')
            plt.ylabel('Ping (ms)')
            plt.xticks(rotation=90)



    lines = ax1.plot(xs,ys)
    f = mdates.DateFormatter('%H:%M:%S')
    ax1.xaxis.set_major_formatter(f)
    mplcursors.cursor(lines,hover=True)
    plt.gcf().autofmt_xdate()
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
