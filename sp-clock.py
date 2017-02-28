import sys
import time
import datetime
import scrollphat

now = datetime.now()
current = now.strftime("%H:%M")

while True:
   try:
        scrollphat.write_string(current)
        time.sleep(1)
   except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
