import random
import time

# caculate the number of points in the unit circle out of n points
def monte_carlo_pi_part(n):
    count = 0
    for i in range(int(n)):
        x = random.random()
        y = random.random()

        # if it is within the unit circle
        if x * x + y * y <= 1:
            count = count + 1

    return count


if __name__ == '__main__':

    # Nummber of points to use for the Pi estimation
    n = 10000000
    start = time.time()
    count = monte_carlo_pi_part(n)
    end = time.time()
    pi = count / (n * 1.0) * 4
    print("Esitmated value of Pi:: %f in %f seconds " % (pi, end-start))