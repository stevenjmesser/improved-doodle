#!/usr/bin/env python

import sys
import time
import scrollphat

scrollphat.clear()
scrollphat.set_brightness(7)
scrollphat.set_rotate(True)

#def scroll_message(message):
#    scrollphat.write_string(message, 11)
#    for x in range(scrollphat.buffer_len()):
#        scrollphat.scroll()
#        time.sleep(0.1)
#        pass
#    scrollphat.clear()

#scroll_message("SET ALARM")
#scroll_message("E.G. 07:00 FOR 7 A.M.")
#scrollphat.write_string("HRS")

#hours = input()

#scrollphat.clear()
#scroll_message("YOU SAID " + hours + " HOURS")
#scrollphat.write_string("MS")

#minutes = input()

#scrollphat.clear()
#scroll_message("YOU SAID " + minutes + " MINUTES")

#scroll_message("I'LL WAKE YOU AT " + hours + ":" + minutes)

while True:
    scrollphat.write_string(time.strftime("%H:%M"), 11)
    scrollphat.scroll()
    time.sleep(0.1)

