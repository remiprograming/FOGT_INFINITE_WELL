import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#step
L = 1**-10
#box dim
x,y = np.linspace(0, L, 200), np.linspace(0, L, 200)
#frames
frames = 10
#path to images
path = f'D:/fizyka/imag/'
#path to outputfile
pathout = f'D:/fizyka/'




#constant
A = (2/L)**0.5


def psi(a, b, s):
    p = (np.sin((s * np.pi * a) / L) * np.sin((s * np.pi * b) / L)) ** 2
    return p





n = 1
for c in range(frames):
    #matrix
    X,Y = np.meshgrid(x,y)
    #?
    psix = np.array([psi(x, y, n) for x, y in zip(np.ravel(X), np.ravel(Y))])
    # compression
    PSI = psix.reshape(X.shape)



    #drawer
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X,Y,PSI, cmap='summer')



    plt.xlabel('X')
    plt.ylabel('Y')
    ax.set_zlabel(f'Klatka {n}')
    print(f'Saved #{n}')
    plt.savefig(f'{path}s{c}.png', transparent=True)
    plt.close()
    n = n + 1




images = [Image.open(f"{path}s{n}.png") for n in range(frames)]
print(f'making gif')


images[0].save(f'{pathout}czonstka{n-1}.gif', save_all=True, append_images=images[1:], duration=300, loop=1)