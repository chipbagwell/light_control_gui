"""Main script for communicating with the LED controller."""

from sense485_hal import setLEDs

__doc__ += (
    """
API:
def outputPins(red, green, green_res, blue):
def off():
def red():
def blu():
def grn():
def grn_res():
def gold():
def yellow():
def purple():
def white():
"""
)


STAIR_RED_PIN = 9
STAIR_BLU_PIN = 8
STAIR_GRN_PIN = 7
STAIR_GRN_RES_PIN = 5

def outputPins(red, green, green_res, blue):
  writePin(STAIR_RED_PIN, not red) 
  writePin(STAIR_GRN_PIN, not green)
  writePin(STAIR_GRN_RES_PIN, not green_res)
  writePin(STAIR_BLU_PIN, not blue)

@setHook(HOOK_STARTUP)
def startupEvent():
  setLEDs(True, True, True) # Green, Blue, Red
  setPinDir(STAIR_GRN_RES_PIN, True)
  setPinDir(STAIR_GRN_PIN, True)
  setPinDir(STAIR_BLU_PIN, True)
  setPinDir(STAIR_RED_PIN, True)
  outputPins(True, True, False, True)

def off():
  outputPins(False, False, False, False)
  setLEDs(False, False, False)

def red():
  outputPins(True, False, False, False)
  setLEDs(False, False, True)

def blu():
  outputPins(False, False, False, True)
  setLEDs(False, True, False)

def grn():
  outputPins(False, True, False, False)
  setLEDs(True, False, False)

def grn_res():
  outputPins(False, False, True, False)
  setLEDs(True, False, False)

def gold():
  outputPins(True, False, True, False)
  setLEDs(True, False, True)

def yellow():
  outputPins(True, True, False, False)
  setLEDs(True, False, True)

def purple():
  outputPins(True, False, False, True)
  setLEDs(False, True, True)

def white():
  outputPins(True, True, False, True)
  setLEDs(True, True, True)

