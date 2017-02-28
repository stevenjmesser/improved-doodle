import sys
import time
import scrollphat

scrollphat.set_brightness(7)
scrollphat.set_rotate(True)

while True:
   try:
        scrollphat.write_string(time.strftime("  "+"%H:%M"+" "))
        scrollphat.scroll()
        time.sleep(0.35)
   except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
