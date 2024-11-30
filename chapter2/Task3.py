import numpy as np

from numba import cuda

print("CUDA devices:", cuda.detect())

@cuda.jit
def vector_add(a, b, c):
    idx = cuda.grid(1)
    if idx < a.size:
        c[idx] = a[idx] + b[idx]


N=1000000
a= np.random.random(N).astype(np.float32)
b= np.random.random(N).astype(np.float32)
C= np.empty(N, dtype=np.float32)

threads_per_block = 256
blocks_per_grid = (a.size + (threads_per_block - 1)) 

vector_add[blocks_per_grid, threads_per_block](a, b, c)

np.testing.assert_almost_equal(c, a + b) 
print("GPU computation successful!")