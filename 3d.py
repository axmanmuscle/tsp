from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np
import matplotlib.pyplot as plt

def neighbor_global(xl, yl):
    rng = np.random.default_rng()
    tmpx = rng.choice(xl)
    tmpy = rng.choice(yl)

    return tmpx.round(2), tmpy.round(2)

def E(z):
    if z < 0:
        return z*z
    return -(z*z)

def P(s, snew, t):
    z = func(s[0], s[1])
    z_new = func(snew[0], snew[1])

    ez = E(z)
    ez_new = E(z_new)

    if ez_new < ez:
        return 1
    else:
        prob = np.exp(-(ez_new - ez) / t)
#        print(prob)
        return prob

def func(x, y):
    return x + 3*np.sin(x)*np.sin(y)

if __name__ == "__main__":

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x = np.arange(-3, 3, 0.1)
    y = np.arange(-3, 3, 0.1)

    X, Y = np.meshgrid(x, y)
#    z = X+3*np.sin(X)*np.sin(Y)
    z = func(X, Y)
    #surf = ax.plot_surface(X, Y, z)
    #plt.show()

    t0 = 30
    dt = 0.1
    num_iter = (t0 - 1) / dt
    t = t0

    x0, y0 = neighbor_global(x, y)

    xt = x0
    yt = y0

    while t > 1:
        t -= dt

        current = [xt, yt]
        xc, yc = neighbor_global(x, y)
        candidate = [xc, yc]

        switch = P(current, candidate, t)

        thresh = np.random.uniform()

        if switch > thresh:
            xt = xc
            yt = yc

        pstr = 'Temperature: {} Value: {}'.format(round(t, 2), round(func(xt, yt),5))
        print(pstr)

    print('Real max (on grid): {}'.format(z.max()))