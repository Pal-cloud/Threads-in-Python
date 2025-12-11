# Tasks for a superhero
# Seqential vs Threads

import threading
import time

def stop_car():
   time_stopping_car = time.sleep(7)
   print("You have stopped a speeding car before it reaches a crowded crosswalk")

def freeze_fire():
   time_freezing_fire = time.sleep(13)
   print("You have freezed a fire to protect a family inside a house")

def hold_balcony():
   time_holding_balcony = time.sleep(10)
   print("You have held a collapsing balcony and everyone has escaped safely")

# Time in sequential execution
start_sequential = time.time()   # initial time in sequential

stop_car()
freeze_fire()
hold_balcony()

end_sequential = time.time()     # final time in sequential

elapsed_sequential = end_sequential - start_sequential
print("------------------------------------------------------------")
print(f"Execution time in sequence: {elapsed_sequential:.2f} seconds")
print("------------------------------------------------------------")
print("                                                            ")


# Time using threads

start_threads = time.time()   # initial time using threads

chore1 = threading.Thread(target=stop_car)
chore1.start()

chore2 = threading.Thread(target=freeze_fire)
chore2.start()

chore3 = threading.Thread(target=hold_balcony)
chore3.start()

#join() ensures that all tasks are completed before proceeding
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete. You are the best!")

end_threads = time.time()     # final time using threads

elapsed_threads = end_threads - start_threads
print("------------------------------------------------------------")
print(f"Execution time using threads: {elapsed_threads:.2f} seconds")
print("------------------------------------------------------------")
print("                                                            ")