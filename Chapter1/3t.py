import numpy as np
from numba import cuda # enable the use of GPU capabilities for computations.
print("CUDA devices:", cuda.detect())
@cuda.jit
def vector_add(a, b, c):
    idx = cuda.grid(1)
    if idx < a.size:
        c[idx] = a[idx] + b[idx]
#Host code
N = 1000000
a = np.random.random(N).astype(np.float32)
b = np.random.random(N).astype(np.float32)
c = np.empty(N, dtype=np.float32)
# Define the number of threads and blocks
threads_per_block = 256
blocks_per_grid = (a.size + (threads_per_block - 1)) // threads_per_block
# Run on the GPU
vector_add[blocks_per_grid, threads_per_block](a, b, c)

# Verify result
np.testing.assert_almost_equal(c, a + b)
print("GPU computation successful!")