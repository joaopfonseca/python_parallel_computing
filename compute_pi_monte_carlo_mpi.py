from mpi4py import MPI
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
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    # Nummber of points to use for the Pi estimation
    n = 10000000
    n_samples = n // size
    start = time.time()

    count = comm.reduce(monte_carlo_pi_part(n_samples), op=MPI.SUM, root=0)
    end = time.time()
    if rank == 0:
        pi = count / (n * 1.0) * 4
        print("Esitmated value of Pi:: %f in %f seconds " % (pi, end-start))
