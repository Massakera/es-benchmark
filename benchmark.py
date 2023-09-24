import timeit
import sys
import es_pyo3
sys.path.append('./python-es')  # Add the directory containing es_client.py to the Python path

import timeit
import es_client

def run_pure_python_query():
    es_client.fetch_complex_query()  # Replace with the actual function name

def run_rs_python_query():
    es_pyo3.fetch_complex_query_py()

avg_time = timeit.timeit(run_pure_python_query, number=100) / 100
avg_tim2 = timeit.timeit(run_rs_python_query, number=100) / 100

print(f"Average time per query for pure Python: {avg_time:.4f} seconds")
print(f"Average time per query for rs python: {avg_tim2:.4f} seconds")

