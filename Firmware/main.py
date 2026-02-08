# This code is for Advanced Human Detector - https://github.com/aoi2010/Advanced_Human_Detector
# MicroPython Code
from machine import Pin, PWM
import time

# =========================
# CONFIGURATION
# =========================

OT2_PIN = 4          # HMMD detection output
BUZZER_PIN = 5       # Passive buzzer (PWM)
BUZZER_FREQ = 2000   # Hz (audible, not harsh)
BUZZER_DUTY = 512    # 50% duty (0–1023)

# Detection filtering
DETECT_CONFIRM_MS = 150    # must stay HIGH for this time
RELEASE_CONFIRM_MS = 300   # must stay LOW for this time
LOOP_DELAY_MS = 20         # main loop delay

# =========================
# HARDWARE SETUP
# =========================

ot2 = Pin(OT2_PIN, Pin.IN)
buzzer = PWM(Pin(BUZZER_PIN))
buzzer.duty(0)              # buzzer OFF at boot
buzzer.freq(BUZZER_FREQ)

# =========================
# STATE VARIABLES
# =========================

last_state = 0              # last stable OT2 state
state_change_time = time.ticks_ms()
buzzer_on = False

# =========================
# HELPER FUNCTIONS
# =========================

def buzzer_enable():
    global buzzer_on
    if not buzzer_on:
        buzzer.duty(BUZZER_DUTY)
        buzzer_on = True

def buzzer_disable():
    global buzzer_on
    if buzzer_on:
        buzzer.duty(0)
        buzzer_on = False

# =========================
# MAIN LOOP
# =========================

while True:
    now = time.ticks_ms()
    current = ot2.value()

    # Detect state change
    if current != last_state:
        state_change_time = now
        last_state = current

    # Confirm detection
    if current == 1:
        if time.ticks_diff(now, state_change_time) >= DETECT_CONFIRM_MS:
            buzzer_enable()
    else:
        if time.ticks_diff(now, state_change_time) >= RELEASE_CONFIRM_MS:
            buzzer_disable()

    time.sleep_ms(LOOP_DELAY_MS)
