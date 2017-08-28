#!/usr/bin/env python3

from pyb00st import movehub

mymovehub = movehub("00:16:53:A4:CD:7E", "hci0")
if mymovehub.is_connected() :
    print("Connection OK")
    print( mymovehub.getAddress() )
    print( mymovehub.getName() )

else:
    print("Connection Failed")