import time
import numpy as np


def Pi_vectorized(num_steps):
    start = time.time()
    step = 1.0 / num_steps
    pi = np.multiply(step, np.sum(np.divide(4.0, np.add(np.square(np.add(np.arange(0,num_steps), 0.5)*step), 1))))
    end = time.time()
    print("Pi with %d steps is %f in %f secs" % (num_steps, pi, end - start))


if __name__ == '__main__':
    Pi_vectorized(100000000)
