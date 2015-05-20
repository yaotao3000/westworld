# -*- coding: UTF-8 -*-
from GameEntity import *
from State import *
import time


bob = Miner(10001)
while 1:
    bob.update()
    time.sleep(0.5)
    


