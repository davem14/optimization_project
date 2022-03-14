import random
import time
from math import inf

from problems import NQueens
from problems import TravelingSalesman
from solvers import HillClimbing, SimulatedAnnealing, TabuSearch

if __name__ == '__main__':
    pr = TravelingSalesman()
    # init = ((1,9), (17,10), (3,7), (20,12), (5,10), (7,11), (5,3), (3,2), (0,4), (6,9), (27,12), (15,23), (22, 17), (1, 23), (11, 10), (21,2))
    # init = ((1,3), (2,5), (2,15), (2,1), (3,3), (7,15), (2,-7), (7,-7))
    # init = ((70, 81), (66, 79), (99, 84), (82, 95), (54, 88), (14, 81), (7, 76), (23, 74), (35, 66), (59, 58), (75, 19), (30, 9), (16, 43), (24, 46), (36, 42), (44, 46), (52, 93), (25, 36), (42, 55), (78, 85))
    init = tuple(set((random.randint(0, 100), random.randint(0, 100)) for _ in range(40)))

    # n = 5
    # pr = NQueens(n)
    # init = tuple(i for i in range(n))

    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    from matplotlib import cm

    iters = [100, 200, 400, 500]
    hoods = [100, 200, 400, 500]

    result = [['122', '109', '2343', '220'],
              ['15', '407', '37', '10'],
              ['100', '100', '100', '100'],
              ['113', '25', '19', '31'],
              ]

    result = np.array(result, dtype=np.int)

    fig = plt.figure(figsize=(5, 5), dpi=150)
    ax1 = fig.add_subplot(111, projection='3d')

    xlabels = np.array(iters)
    xpos = np.arange(xlabels.shape[0])
    ylabels = np.array(hoods)
    ypos = np.arange(ylabels.shape[0])

    xposM, yposM = np.meshgrid(xpos, ypos, copy=False)

    zpos = result
    zpos = zpos.ravel()

    dx = 0.5
    dy = 0.5
    dz = zpos

    ax1.w_xaxis.set_ticks(xpos + dx / 2.)
    ax1.w_xaxis.set_ticklabels(xlabels)

    ax1.w_yaxis.set_ticks(ypos + dy / 2.)
    ax1.w_yaxis.set_ticklabels(ylabels)

    ax1.set_xlabel('Iterations')
    ax1.set_ylabel('Hoods')
    ax1.set_zlabel('Cost')

    values = np.linspace(0.2, 1., xposM.ravel().shape[0])
    colors = cm.rainbow(values)
    ax1.bar3d(xposM.ravel(), yposM.ravel(), dz * 0, dx, dy, dz, color=colors)
    plt.show()


    for i in range(4):
        for h in range(4):


            for solver in [
                # HillClimbing(pr, init, batch_size=inf),
                # SimulatedAnnealing(pr, init, cooling_factor=.9),
                TabuSearch(pr, init, max_iterations=iters[i], batch_size=hoods[h])
            ]:
                t = time.time()
                solution = solver()
                print(pr.evaluate(solution), time.time() - t, "iters=", iters[i], "hood=",hoods[h])
                result[i][h] = pr.evaluate(solution)
                # pr.show(solution)
                # input("press enter to exit")

    result = np.array(result, dtype=np.int)

    fig = plt.figure(figsize=(5, 5), dpi=150)
    ax1 = fig.add_subplot(111, projection='3d')

    xlabels = np.array(iters)
    xpos = np.arange(xlabels.shape[0])
    ylabels = np.array(hoods)
    ypos = np.arange(ylabels.shape[0])

    xposM, yposM = np.meshgrid(xpos, ypos, copy=False)

    zpos = result
    zpos = zpos.ravel()

    dx = 0.5
    dy = 0.5
    dz = zpos

    ax1.w_xaxis.set_ticks(xpos + dx / 2.)
    ax1.w_xaxis.set_ticklabels(xlabels)

    ax1.w_yaxis.set_ticks(ypos + dy / 2.)
    ax1.w_yaxis.set_ticklabels(ylabels)

    ax1.set_xlabel('Iterations')
    ax1.set_ylabel('Hoods')
    ax1.set_zlabel('Cost')

    values = np.linspace(0.2, 1., xposM.ravel().shape[0])
    colors = cm.rainbow(values)
    ax1.bar3d(xposM.ravel(), yposM.ravel(), dz * 0, dx, dy, dz, color=colors)
    plt.show()