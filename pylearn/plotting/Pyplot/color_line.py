import matplotlib.pyplot as plt

def myplot(x, y, fname=None, **kwargs):
    "make plot of x,y. save to fname if not None. Provide kwargs to plot."
    plt.plot(x, y, **kwargs)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('My plot')
    if fname:
        plt.savefig(fname)
    else:
        plt.show()

x = [1, 3, 4, 5]
y = [3, 6, 9, 12]

myplot(x, y, None, color='orange', marker='s')

# you can use a dictionary as kwargs
d = {'color':'magenta',
     'marker':'d'}

myplot(x, y, None, **d)