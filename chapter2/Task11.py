import numpy as np
from concurrent.futures import ThreadPoolExecutor 
import time
import random
import empty

def vector_add_slice(start, end, a, b, c):
    c[start:end] = a[start:end] + b[start:end]


N = 1000000
a = np.random.random(N).astype(np.float32) 
b = np.random.random(N).astype(np.float32) 
C = np.empty(N, dtype=np.float32)

threads = 8  
chunk_size = N // threads

start_time = time.time()

with ThreadPoolExecutor(max_workers=threads) as executor:
    futures = []
    for i in range (threads):
        start = i * chunk_size
        end = N if i == threads - 1 else (i + 1) * chunk_size
        futures.append(executor.submit(vector_add_slice, start, end, a, b, c))

    for future in futures:
        future.result()

end_time = time.time()

print (f"Time taken for parallel computation: {end_time - start_time:.5f} seconds")

np.testing.assert_almost_equal(c, a + b) 
print(f"First 10 elements of result: {c[:10]}")