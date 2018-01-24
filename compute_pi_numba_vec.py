from numba import vectorize
from numba import jit
import time
import numpy as np


def Pi(num_steps):
    start = time.time()
    step = 1.0 / num_steps
    sum = 0

    for i in range(num_steps):
        x = (i + 0.5) * step
        sum = sum + 4.0 / (1.0 + x * x)

    pi = step * sum
    end = time.time()
    print("Pi with %d steps is %f in %f secs" % (num_steps, pi, end - start))


@vectorize('float64(int64)', target='parallel')
def Pi_numba_vec(num_steps):
    step = 1.0 / num_steps
    pi = np.multiply(step, np.sum(np.divide(4.0, np.add(np.square(np.add(np.arange(0,num_steps), 0.5)*step), 1))))
    return pi


if __name__ == '__main__':
    Pi_numba = jit(Pi)
    num_steps = 100000000
    Pi(num_steps)
    Pi_numba(num_steps)
    start = time.time()
    pi = Pi_numba_vec(num_steps)
    end = time.time()
    print("Pi with %d steps is %f in %f secs" % (num_steps, pi, end - start))