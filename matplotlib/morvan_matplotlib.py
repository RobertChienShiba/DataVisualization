# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:33:30 2021

@author: rober
"""

# import matplotlib.pyplot as plt

# fig = plt.figure()
# x = [1, 2, 3, 4, 5, 6, 7]
# y = [1, 3, 4, 2, 5, 8, 6]

# # below are all percentage
# left, bottom, width, height = 0.1, 0.1, 1., 1.0
# ax1 = fig.add_axes([left, bottom, width, height])  # main axes
# ax1.plot(x, y, 'r')
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.set_title('title')

# ax2 = fig.add_axes([0.2, 0.7, 0.25, 0.25])  # inside axes
# ax2.plot(y, x, 'b')
# ax2.set_xlabel('x')
# ax2.set_ylabel('y')
# ax2.set_title('title inside 1')


# # different method to add axes
# ####################################
# plt.axes([0.8, 0.2, 0.25, 0.25])
# plt.plot(y[::-1], x, 'g')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('title inside 2')

#plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(0, 10, 0.1)
# y1 = 0.05 * x**2
# y2 = -1 *y1


# fig, ax1 = plt.subplots()

# ax2 = ax1.twinx()    # mirror the ax1
# ax1.scatter(x, y1,  marker = '.',color="r")
# ax2.scatter(x,y2, marker = '.')

# ax1.set_xlabel('X data')
# ax1.set_ylabel('Y1 data', color='g')
# ax2.set_ylabel('Y2 data', color='b')


# plt.show()


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


#fig, ax = plt.subplots()
#x = np.arange(0, 2*np.pi, 0.1)
# line,= ax.plot(x, np.sin(x))
x=0
x_list=[]


def animate(i):
    global x
    plt.cla()
    x_list.append(x)
    plt.plot(x_list, np.sin(x_list),label="$sin(x)$")
    x+=0.25
    #line.set_ydata(np.sin(x + i/10)) # update the data
    #return line,
    plt.ylim(-1.25,1.25)
    plt.legend(loc='upper left')
    plt.tight_layout()

# Init only required for blitting to give a clean slate.
# def init():
#     line.set_ydata(np.sin(x))
#     return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
# blit=True dose not work on Mac, set blit=False
# interval= update frequency
ani = animation.FuncAnimation(plt.gcf(), func=animate,interval=20)#,init_func=init,blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

#plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = Axes3D(fig)
# X = np.arange(-4, 4, 0.25)
# #print(X.shape)
# Y = np.arange(-4, 4, 0.25)
# #print(Y.shape)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X ** 2 + Y ** 2)
# #print(R)
# # height value
# Z = np.sin(R)

# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
# ax.set_zlim(-2,2)
# plt.show()
        

# import matplotlib.pyplot as plt
# import numpy as np

# def f(x,y):
#     # the height function
#     #print(1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)
#     return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

# n = 256
# x = np.linspace(-3, 3, n)
# y = np.linspace(-3, 3, n)
# X,Y = np.meshgrid(x, y)
# # use plt.contourf to filling contours
# # X, Y and value for (X,Y) point
# plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
# C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidths=.5)
# plt.clabel(C, inline=True, fontsize=10)
# plt.xticks(())
# plt.yticks(())
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(-3, 3, 50)
# y1 = 2*x + 1
# y2 = x**2

# plt.figure()
# plt.plot(x, y2)
# # plot the second curve in this figure with certain parameters
# plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
# # set x limits
# plt.xlim((-1, 2))
# plt.ylim((-2, 3))

# # set new ticks
# new_ticks = np.linspace(-1, 2, 5)
# plt.xticks(new_ticks)
# # set tick labels
# plt.yticks([-2, -1.8, -1, 1.22, 3],labels=
#            ['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])
# # to use '$ $' for math text and nice looking, e.g. '$\pi$'

# # gca = 'get current axis'
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')

# ax.xaxis.set_ticks_position('bottom')
# # ACCEPTS: [ 'top' | 'bottom' | 'both' | 'default' | 'none' ]

# ax.spines['bottom'].set_position(('data', 0))
# # the 1st is in 'outward' | 'axes' | 'data'
# # axes: percentage of y axis
# # data: depend on y data

# ax.yaxis.set_ticks_position('left')
# # ACCEPTS: [ 'left' | 'right' | 'both' | 'default' | 'none' ]

# ax.spines['left'].set_position(('data',0))
#plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(-3, 3, 50)
# y = 2*x + 1

# plt.figure(num=1, figsize=(8, 5),)
# plt.plot(x, y,)

# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data', 0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data', 0))

# x0 = 1
# y0 = 2*x0 + 1
# plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
# plt.scatter(x0, y0, s=100, color='b')

# # method 1:
# #####################
# plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
#               textcoords='offset points', fontsize=16,
#               arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

# # method 2:
# ########################
# plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
#           fontdict={'size': 16, 'color': 'r'})

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(-3, 3, 50)
# y = 0.1*x

# plt.figure()
# plt.plot(x, y, linewidth=10, zorder=1)      # set zorder for ordering the plot in plt 2.0.2 or higher
# plt.ylim(-2, 2)
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data', 0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data', 0))


# for label in ax.get_xticklabels() + ax.get_yticklabels():
#     #print(ax.get_xticklabels() + ax.get_yticklabels())
#     label.set_fontsize(12)
#     # set zorder for ordering the plot in plt 2.0.2 or higher
#     label.set_bbox(dict(facecolor='w', edgecolor='none', alpha=0.8))
# plt.show()