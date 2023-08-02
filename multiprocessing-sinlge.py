import multiprocessing
import time
 
def task():
    print('Sleeping for 0.5 seconds')
    time.sleep(0.5)
    print('Finished sleeping')
 
if __name__ == "__main__":
    start = time.time()
 
    # Creates two processes
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
 
    # Starts both processes
    p1.start()
    p2.start()
    
        # Joins all the processes 
    for p in processes:
        p.join()
 
    end = time.time()
 
    print(f"Program finished in {start-end} seconds")