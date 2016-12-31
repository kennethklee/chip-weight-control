#!/usr/bin/env python3

import os

from time import sleep
from subprocess import call

GPIO = '1016'
GPIO_FILENAME = '/sys/class/gpio/gpio' + GPIO + '/value'

WII_WEIGHT_SCRIPT_PATH = '/home/chip/.homeassistant/scripts/wii-weight.py'

def read_edge(previous, interval=0.2):
  last_value = previous

  while True:
    if os.path.isfile(GPIO_FILENAME):
      with open(GPIO_FILENAME, 'r') as f:
        value = f.read().rstrip()

      if last_value != value:
        last_value = value
        return value
  
    sleep(interval)

if __name__ == "__main__":
  last_value = '1'
  
  while True:
    value = read_edge(last_value)
    if value == '1':
      call(['python', WII_WEIGHT_SCRIPT_PATH])
    last_value = value

