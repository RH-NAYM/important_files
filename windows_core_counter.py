import multiprocessing
import uvicorn
def get_number_of_workers():
    num_cpus = multiprocessing.cpu_count()

    return num_cpus * 2 + 1

if __name__ == "__main__":
    num_workers = get_number_of_workers()
    print("Number of workers : ",num_workers)
