import sys
import time
import scrollphat

current = now.strftime("%H:%M")

while True:
   try:
        scrollphat.write_string(current)
        time.sleep(1)
   except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
