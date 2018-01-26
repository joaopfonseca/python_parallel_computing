import time
from numba import jit
from mpi4py import MPI

@jit
def Pi(num_steps, rank, size):
    step = 1.0 / num_steps
    sum = 0

    for i in range(rank, num_steps, size):
        x = (i + 0.5) * step
        sum = sum + 4.0 / (1.0 + x * x)

    pi = step * sum

    return pi


if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    if rank == 0:
        n = 100000000000
    else:
        n = None

    start = time.time()
    n = comm.bcast(n, root=0)

    local_pi = Pi(n, rank, size)
    pi = comm.reduce(local_pi, op=MPI.SUM, root=0)
    end = time.time()
    if rank == 0:
        print("Esitmated value of Pi:: %f in %f seconds " % (pi, end - start))