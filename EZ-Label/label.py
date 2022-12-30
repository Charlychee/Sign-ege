import matplotlib.pyplot as plt

ax = plt.gca()
fig = plt.gcf()
implot = ax.imshow(plt.imread('img.png'))


def onclick(event):
    if event.xdata != None and event.ydata != None:
        print(event.xdata, event.ydata)


cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
