import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

array_size = 3
recvdata = np.zeros(array_size, dtype=np.int)
senddata = (rank + 1) * np.arange(array_size, dtype=np.int)

print(" process %s sending %s " % (rank, senddata))
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)
print("on task %d after Reduce: data = %s" % (rank, recvdata))
