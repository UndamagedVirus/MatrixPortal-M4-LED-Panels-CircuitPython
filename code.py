# SPDX-FileCopyrightText: 2020 John Park for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Quote board matrix display
# uses AdafruitIO to serve up a quote text feed and color feed
# random quotes are displayed, updates periodically to look for new quotes
# avoids repeating the same quote twice in a row
import time
from time import localtime
import board
import terminalio
import rtc
import busio
from adafruit_matrixportal.matrixportal import MatrixPortal
from adafruit_matrixportal.network import Network

SCROLL_DELAY = 0.06

rtc = rtc.RTC()
TIMEZONE = 0



# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise
print("Time will be set for {}".format(secrets["timezone"]))

#print(time.localtime)

def _format_datetime(datetime):
    return "{:02}/{:02}/{} {:02}:{:02}:{:02}".format(
        datetime.tm_mday,
        datetime.tm_mon,
        datetime.tm_year,
        datetime.tm_hour,
        datetime.tm_min,
        datetime.tm_sec,
    )

print("This Is Monotonic: ")
rtc.datetime = time.localtime(time.time() + TIMEZONE * 3600)
print("RTC timestamp: {}".format(_format_datetime(rtc.datetime)))
print("Local time: {}".format(_format_datetime(time.localtime())))

# --- Display setup ---
matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=True)


name1_label = matrixportal.add_text(
    text_font=terminalio.FONT,
    text_scale=1,
    text_color=0xFFFFFF,
    text_position=(1, 5),
    scrolling=True,
    text_anchor_point=(0, 0.5),
    
)


name2_label = matrixportal.add_text(
    text_font=terminalio.FONT,
    text_scale=1,
    text_color=0xFFFFFF,
    #text_position=(matrixportal.graphics.display.width // 2, -2),
    text_position=(1, 16),
    #text_anchor_point=(0.5, 0),
)


name3_label = matrixportal.add_text(
    text_font=terminalio.FONT,
    text_scale=1,
    text_color=0x0B5394,
    #text_position=(matrixportal.graphics.display.width // 2, 24),
    #text_anchor_point=(1, 0.5),
    text_position=(0, 27),
    scrolling=False,
)



matrixportal.set_text("Print Progress:", name1_label),
matrixportal.set_text("EMT", name2_label),
matrixportal.set_text("HA", name3_label),

matrixportal.scroll_text(SCROLL_DELAY),

print(rtc.datetime)

while True: 
    pass
    matrixportal.scroll()
    time.sleep(SCROLL_DELAY)
    current = time.monotonic()
    

#while True:
#    cpu_temp = microcontroller.cpu.temperature
#    temp_value.text = f"{cpu_temp:.1f} C"
#    time.sleep(0.5)