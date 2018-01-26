import numpy as np
import time

# caculate the number of points in the unit circle out of n points
def monte_carlo_pi_part(samples):
    count = 0
    for x, y in samples:
        # if it is within the unit circle
        if x * x + y * y <= 1:
            count = count + 1

    return count


if __name__ == '__main__':

    # Nummber of points to use for the Pi estimation
    n = 10000000
    start = time.time()
    samples = np.random.random((n, 2))
    count = monte_carlo_pi_part(samples)
    end = time.time()
    pi = count / (n * 1.0) * 4
    print("Esitmated value of Pi:: %f in %f seconds " % (pi, end-start))