import sys
import time
import scrollphat

scrollphat.set_brightness(50)
scrollphat.set_rotate(True)
current = time.strftime("  "+"%H:%M"+" ")

while True:
   try:
        scrollphat.scroll()
        scrollphat.write_string(current)
        time.sleep(0.35)
   except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
