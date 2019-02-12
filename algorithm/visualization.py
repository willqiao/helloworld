from matplotlib import pyplot


fig = pyplot.figure("My Job")
ax = fig.add_subplot(1,1,1)
ax.hist([2,3,4,5,6,7,8])
pyplot.show()