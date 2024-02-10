import multiprocessing

def get_number_of_workers():
    # Get the number of CPU cores
    num_cpus = multiprocessing.cpu_count()
    
    # You may adjust this formula based on your specific requirements
    # For example, you could use num_cpus * 2 or any other heuristic
    return num_cpus

if __name__ == "__main__":
    print(get_number_of_workers())



# cmd: lscpu



"""
import os

def get_number_of_cpu_cores():
    try:
        # Read the number of CPU cores from /proc/cpuinfo
        with open('/proc/cpuinfo') as f:
            cpu_info = f.read()

        # Count the number of lines containing 'processor' in the cpuinfo
        num_cores = cpu_info.count('processor')
        return num_cores
    except Exception as e:
        print(f"Error reading CPU information: {e}")
        return None

if __name__ == "__main__":
    num_cpus = get_number_of_cpu_cores()
    print(f"Number of CPU cores: {num_cpus}")
    

import multiprocessing
import uvicorn
from main import app

def get_number_of_workers():
    num_cpus = multiprocessing.cpu_count()
    return num_cpus * 2 + 1

if __name__ == "__main__":
    num_workers = get_number_of_workers()
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=num_workers)

"""
