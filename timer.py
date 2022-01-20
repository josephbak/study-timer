import time
import sys
import os
from beepy import beep

work_time_with_unit = input("Type the working time with a number followed by m or s: ")
rest_time_with_unit = input("Type the resting time with a number followed by m or s: ")
cycle_num = input("How many cycles? ")

if work_time_with_unit == "":
    work_time_with_unit = "5s"
if rest_time_with_unit == "":
    rest_time_with_unit = "2s"
if cycle_num == "":
    cycle_num = 2
else:
    cycle_num = int(cycle_num)

CYCLE_LEFT = cycle_num

working_time_unit = work_time_with_unit[-1]
working_time = int(work_time_with_unit[:-1])
rest_time_unit = rest_time_with_unit[-1]
resting_time = int(rest_time_with_unit[:-1])

def time_disply(total_time, unit, flag):
    global CYCLE_LEFT
    # column_size = os.get_terminal_size().columns
    # print(column_size)

    # time given in minutes
    if unit in ["m", "M"]:
        total_time = total_time * 60

    sec = total_time

    # pound_num_per_second = (sec-21) // column_size
    # print(pound_num_per_second)
    # pound_num_leftover = (sec-21) % column_size


    if flag in ["w", "W"]: # while working
        while sec > 0:
            m, s = divmod(sec, 60)
            h, m = divmod(m, 60)
            # print(f"\rWorking time",f"{int(h)}".rjust(2, '0'), f"{int(m)}".rjust(2, '0'),
            #       f"{int(s)}".rjust(2, '0'), sep=':', end='')
            sys.stdout.write("\r")
            sys.stdout.write(f"Working time||{str(h).rjust(2, '0'):2s}:{str(m).rjust(2, '0'):2s}:{str(s).rjust(2, '0'):2s}")
            # sys.stdout.write(f"{'*'*pound_num_per_second*(total_time - sec + 1)}")
            sys.stdout.flush()
            sec -= 1
            time.sleep(1)
    else:
        while sec > 0:
            m, s = divmod(sec, 60)
            h, m = divmod(m, 60)
            # print(f"\rResting time",f"{int(h)}".rjust(2, '0'), f"{int(m)}".rjust(2, '0'),
            #       f"{int(s)}".rjust(2, '0'), sep=':', end='')
            sys.stdout.write("\r")
            sys.stdout.write(f"Resting time||{str(h).rjust(2, '0'):2s}:{str(m).rjust(2, '0'):2s}:{str(s).rjust(2, '0'):2s}")
            # sys.stdout.write(f"{'*'*pound_num_per_second*(total_time - sec + 1)}")
            sys.stdout.flush()
            sec -= 1
            time.sleep(1)
        else:
            print(f"\r  Cycle {CYCLE_LEFT}/{cycle_num} Completed !  ")
        CYCLE_LEFT -= 1

while CYCLE_LEFT >= 0:
    if CYCLE_LEFT == 0:
        print("It's done! Well done!")
        break
    else:
        time_disply(working_time, working_time_unit, "w")
        beep(sound='ping')
        input("Press Enter to continue.")
        time_disply(resting_time, rest_time_with_unit, "r")
        beep(sound='ping')





# for remaining in range(10, 0, -1):
#     sys.stdout.write("\r")
#     sys.stdout.write("{:2d} seconds remaining.".format(remaining))
#     sys.stdout.flush()
#     time.sleep(1)
#
# sys.stdout.write("\rComplete!            \n")