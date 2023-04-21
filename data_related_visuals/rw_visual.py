from random_walk import RamdonWalk
import matplotlib.pyplot as plt
i=1
while i < 2:
    rw = RamdonWalk()
    rw.fill_walk()

    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot (rw.x_values, rw.y_values, linewidth=2)
    #ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    i+=1

