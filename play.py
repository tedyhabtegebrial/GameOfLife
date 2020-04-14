import time
import random
import argparse
import scipy
from scipy import ndimage as ndi

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from shapes import addGlider, addGosperGliderGun

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--num_generations', type=int, default=500)
arg_parser.add_argument('--world_size', type=int, default=80)
arg_parser.add_argument('--sleep_time', type=float, default=0.02)
opts = arg_parser.parse_args()

gofl_kernel = np.ones((3,3), dtype=np.float32)
gofl_kernel[1,1] = 0.0

world = np.zeros((opts.world_size, opts.world_size), dtype=np.float32)
world = addGlider(2,2, world)
world = addGosperGliderGun(20,20, world)

fig, ax = plt.subplots()
text = plt.text(opts.world_size-10,opts.world_size-10,f'Generation {0}')
for itr in range(opts.num_generations):
    im = ax.imshow(world, interpolation='nearest', cmap=cm.binary, vmax=1, vmin=0)
    plt.pause(opts.sleep_time)
    text.set_text(f'Generation {itr}')
    new_world = ndi.correlate(world, gofl_kernel, mode='wrap')
    world[new_world<2.0] = 0
    world[new_world>3.0] = 0
    world[new_world==3.0] = 1
plt.show()
