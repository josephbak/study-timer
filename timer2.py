import sys  
import time


for remaining in range(10, 0, -1):
     sys.stdout.write("\r")
     sys.stdout.write(f"{remaining:2d} seconds remaining.")#.format(remaining))
     sys.stdout.flush()
     time.sleep(1)

sys.stdout.write("\rComplete!            \n")
