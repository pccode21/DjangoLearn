import matplotlib.pyplot as plt
import numpy as np

def plot_line_sine():
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.plot([1,2,3,4], [4,5,2,1])
    ax2 = fig.add_subplot(122)
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    ax2.plot(x, y)
    return fig


def image_plot():
    """ plt.imshow demonstration

    Source:

        https://matplotlib.org/3.1.0/gallery/images_contours_and_fields/image_demo.html

    """

    delta = 0.025
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
    Z = (Z1 - Z2) * 2
    fig, ax = plt.subplots()
    im = ax.imshow(Z, interpolation='bilinear', cmap='RdYlGn',
                origin='lower', extent=[-3, 3, -3, 3],
                vmax=abs(Z).max(), vmin=-abs(Z).max()
            )
    return fig


def plot_with_args(x, y):
    """ Pass arguments to plot function """

    fig, ax = plt.subplots()
    plt.plot(x, y)
    return fig


def countour_plot(custom_title):
    """ Contour plot demo

    Source:
        https://matplotlib.org/3.1.1/gallery/images_contours_and_fields/contour_demo.html

    """

    delta = 0.025
    x = np.arange(-3.0, 3.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
    Z = (Z1 - Z2) * 2
    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, Z)
    ax.clabel(CS, inline=1, fontsize=10)
    ax.set_title(custom_title)
    return fig
