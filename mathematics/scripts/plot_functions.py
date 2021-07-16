
import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r'C:\考研\微积分\notes\graphics')

#  绘制 y=xln(x) 观察 x=0 处其切线斜率为负无穷，导数不存在
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# x = np.linspace(0.001, 5, 100)
# y = x * np.log(x)
# ax.plot(x, y,)  # Plot some data on the axes.
# plt.title(r'$y=x\ln x$')
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.5) # these are matplotlib.patch.Patch properties
# textstr = r'$f(0_+)\to -\infty$ (non-differentiable)'
# ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
#         verticalalignment='top', bbox=props) # place a text box in upper left in axes coords
# plt.savefig('xlnx.png', dpi=600, format='png')

# plt.show(fig)
# plt.close(fig)

# 绘制 y=sin(x)/(exp(x)+c) 观察 x=0 处极限随着 c 的变化
fig, ax = plt.subplots()  # Create a figure containing a single axes.
x = np.linspace(-0.01, 0.01, 100)

c = -1
y = np.sin(x)/(np.exp(x)+c)
ax.plot(x, y, label=r'$c=-1$')  # Plot some data on the axes.
c = -1.05
y = np.sin(x)/(np.exp(x)+c)
ax.plot(x, y, label=r'$c=-1.05$')  # Plot some data on the axes.
c = -0.95
y = np.sin(x)/(np.exp(x)+c)
ax.plot(x, y, label=r'$c=-0.95$')  # Plot some data on the axes.
c = 0
y = np.sin(x)/(np.exp(x)+c)
ax.plot(x, y, label=r'$c=0$')  # Plot some data on the axes.
c = -2
y = np.sin(x)/(np.exp(x)+c)
ax.plot(x, y, label=r'$c=-2$')  # Plot some data on the axes.
# yposition = [0, 1]
# for yc in yposition:
#     plt.axhline(y=yc, color='k', linestyle='--')
xposition = 0
plt.axvline(x=xposition, color='k', linestyle='--')
ax.legend()
ax.plot()
plt.title(r'$y=\dfrac{\sin x}{\mathrm{e}^x + c}$')
plt.savefig('2.png', dpi=600, format='png')
