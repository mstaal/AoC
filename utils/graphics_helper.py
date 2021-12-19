import matplotlib.pyplot as plt


def plot_data(x, y, z=[], w=[]):
    fig = plt.figure()
    if len(z) > 0:
        ax = fig.add_subplot(111, projection='3d')
        if len(w) > 0:
            img = ax.scatter(x, y, z, c=w, cmap=plt.hot())
            fig.colorbar(img)
        else:
            ax.scatter(x, y, z)
    else:
        plt.scatter(x, y)
    plt.show()
