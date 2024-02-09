import multiprocessing
import uvicorn
def get_number_of_workers():
    num_cpus = multiprocessing.cpu_count()

    return num_cpus * 2 + 1

if __name__ == "__main__":
    num_workers = get_number_of_workers()
    print("Number of workers : ",num_workers)


"""
import multiprocessing

def get_number_of_workers():
    # Get the number of CPU cores
    num_cpus = multiprocessing.cpu_count()
    
    # You may adjust this formula based on your specific requirements
    # For example, you could use num_cpus * 2 or any other heuristic
    return num_cpus

if __name__ == "__main__":
    print(get_number_of_workers())


"""
