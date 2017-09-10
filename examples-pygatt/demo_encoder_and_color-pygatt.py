#!/usr/bin/env python3

from pyb00st_pygatt.movehub import MoveHub
from pyb00st_pygatt.constants import *

from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)
mymovehub.subscribe_all()
mymovehub.listen_encoder_sensor(PORT_D)
mymovehub.listen_color_sensor(PORT_C)

while True:
    sleep(0.2)
    print('Motor D: {} Color: {}'.format(mymovehub.last_encoder_D, mymovehub.last_color_C))
