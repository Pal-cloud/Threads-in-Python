# multithreading = Used to perform multiple tasks at the same time
# Good for I/O bound tasks like reading files or fetching data from APIs
# threading.Thread(target=my_function)
# Sequential tasks for a superhero
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