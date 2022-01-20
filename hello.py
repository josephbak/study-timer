from beepy import beep
import sys, time

## Create the variable _TIME from sys.argv or wherever, make sure it is a valid
# float, > 0, etc etc
## Depends on how you expect input

# _TIME = 10 # Just for example, remove this

# while _TIME > 0:
#     m, s = divmod(_TIME, 60)
#     h, m = divmod(m, 60)
#     print(f"\r{int(h)}".rjust(2,'0'), f"{int(m)}".rjust(2,'0'),
#             f"{int(s)}".rjust(2,'0'), sep=':', end='')
#     _TIME -= 0.001
#     time.sleep(0.001)
# else:
#     print("\r  Completed !  ")


# def beep():
#     print("\a")

# beep()


beep(sound='coin')
time.sleep(1)
# beep(sound='robot_error')
# time.sleep(1)
# beep(sound='error')
# time.sleep(1)
beep(sound='ping')
time.sleep(1)
# beep(sound='ready')
# time.sleep(1)
# beep(sound='success')
# time.sleep(1)
# beep(sound='wilhelm')
# time.sleep(1)
