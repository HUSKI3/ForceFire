#build modules for forcefire

print("Welcome to ForceFire!")
print("Building in process!")

#imports
import itertools
import threading
import time
import sys
import os

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     \n')

# Create build directory
t = threading.Thread(target=animate)
t.start()
path = "./forcefire/build"
os.makedirs(path)
done = True
print("created /force/build/ ")
# END

# Create modules for instance


# Create template instance file
t = threading.Thread(target=animate)
t.start()
()
done = True
print("created build/intance/template.ff ")

#Starting build for instance